# Generated by Django 3.0.4 on 2021-11-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0442_auto_20211115_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_receipts',
            name='wamount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='WAmount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
