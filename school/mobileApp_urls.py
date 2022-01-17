from django.conf.urls import url, include
from . import mobileApp_views
from django.conf import settings

urlpatterns = [
    url(r'CustomerDetails/', mobileApp_views.CustomerDetails),
    url(r'CreateNewReciept/', mobileApp_views.CreateNewReciept),
    url(r'RecieptDetails/(?P<custCode>.*)/$', mobileApp_views.RecieptDetails),
]
