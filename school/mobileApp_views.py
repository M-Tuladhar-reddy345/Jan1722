from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
import datetime

from .models import Customer, saleorder, daily_pic_receipts


def CustomerDetails(request):
    brch = 'Raithanna'
    customer_list = []
    customer_query = 'select distinct S.id, C.custCode custcode, C.custName, sum(OSAmount) osamt from  %s.school_saleorder S,  %s.school_customer C where C.custCode = S.custcode and netAmount > 0 and osAmount > 0 group by C.custCode order by C.custName ' % (
        str(brch), str(brch))
    # getSalesData = "select distinct S.id, C.custCode custcode, C.custName, sum(OSAmount) osamt from  %s.school_saleorder S,  %s.school_customer C where C.custCode = S.custcode and netAmount > 0 and osAmount > 0 group by C.custCode order by C.custName "%(str(brch),str(brch))
    Customers = saleorder.objects.using(brch).raw(customer_query)
    for i in Customers:
        customer_list.append({
            'custName': i.custName,
            'custCode': i.custcode,
            'Osamt': i.osamt, })

    return JsonResponse({'results': customer_list}, safe=False)


@csrf_exempt
def RecieptDetails(request, custCode):
    brch = 'Raithanna'
    customer_query = 'select distinct S.id, C.custCode custcode, C.custName, sum(OSAmount) osamt from  %s.school_saleorder S,  %s.school_customer C where S.custcode = "%s" and C.custCode = S.custcode and netAmount > 0 and osAmount > 0 group by C.custCode order by C.custName ' % (
        str(brch), str(brch), str(custCode))
    Customer = saleorder.objects.using(brch).raw(customer_query)
    Reciepts = daily_pic_receipts.objects.using(brch).all()

    context = {"RecieptNo": len(Reciepts)+1,
               "Rectypes": ['Cash', 'Checkque'],
               "payRefNo": '',
               "RecAmt": Customer[0].osamt,
               "Waiver": 0,
               "Remarks": '',
               }

    return JsonResponse(context, safe=False)


@csrf_exempt
def CreateNewReciept(request):
    try:
        brch = 'Raithanna'
        if request.method == 'POST':
            data = request.POST
            RecieptNo = data['RecieptNo']
            date = data['Date']
            RecType = data['Rectype']
            PayRefNo = data['payRefNo']
            RecAmt = data['RecAmt']
            Waiver = data['Waiver']
            Remarks = data['Remarks']
            custcode = data['Custcode']
            customer_query = 'select distinct S.id, C.custCode custcode, C.custName, sum(OSAmount) osamt from  %s.school_saleorder S,  %s.school_customer C where S.custcode = "%s" and C.custCode = S.custcode and netAmount > 0 and osAmount > 0 group by C.custCode order by C.custName ' % (
                str(brch), str(brch), str(custcode))
            Customer = saleorder.objects.using(brch).raw(customer_query)
            if int(RecAmt)+int(Waiver) > Customer[0].osamt:
                return JsonResponse('Rec Amt cannot excceed os amt', safe=False)
            details_form = daily_pic_receipts.objects.using(brch).create(
                branch=brch,
                recNo=int(RecieptNo),
                # orderNo = request.POST.getlist('OrderNo[]')[index],
                recdate=date,
                recType=RecType,
                payRefNo=PayRefNo,
                amount=int(RecAmt),
                wamount=int(Waiver),
                remarks=Remarks,
                entryDate=datetime.datetime.today(),
                # entryUser = request.user.username,
                custcode=custcode,
                # created_by=request.user,
            )
            try:
                details_form.save()
                return JsonResponse(f'Success create receipt {RecieptNo}', safe=False)
            except:
                return JsonResponse(f'Failure create receipt {RecieptNo}', safe=False)
        return None
    except Exception as e:
        print('@84 '+e)
        return JsonResponse(e, safe=False)

# Create your views here.


# def login(request):
#     branch = Branch.objects.all().values('code').distinct().order_by(('code'))
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         branch = request.POST['branch']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             if request.POST['branch'] == user.extendeduser.branch:
#                 auth.login(request, user)
#                 request.session['name'] = request.POST['username']
#                 if user.extendeduser.role == 'Admin':
#                     group = Group.objects.get(name='Admin')
#                     user.groups.add(group)
#                 elif user.extendeduser.role == 'Manager':
#                     group = Group.objects.get(name='Manager')
#                     user.groups.add(group)
#                 else:
#                     group = Group.objects.get(name='Operator')
#                     user.groups.add(group)
#                 return render(request, 'home.html', locals())
#             else:
#                 messages.info(request, 'Invalid Branch Credentials')
#                 return redirect('/login/')
#         else:
#             messages.info(request, 'Invalid Credentials')
#             return redirect('/login/')

#     else:
#         return render(request, 'login.html', locals())
