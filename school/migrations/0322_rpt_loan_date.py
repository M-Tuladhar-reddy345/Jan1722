# Generated by Django 3.2 on 2021-06-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0321_remove_rpt_loan_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_loan',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]