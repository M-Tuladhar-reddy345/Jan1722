# Generated by Django 3.2 on 2021-06-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0335_rpt_loan_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_loan',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]