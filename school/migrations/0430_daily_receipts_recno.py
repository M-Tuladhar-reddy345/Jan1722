# Generated by Django 3.0.4 on 2021-10-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0429_auto_20211028_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_receipts',
            name='recNo',
            field=models.IntegerField(default=0),
        ),
    ]