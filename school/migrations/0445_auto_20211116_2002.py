# Generated by Django 3.0.4 on 2021-11-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0444_prodmaster_milkunits'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_sales',
            name='entryDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='daily_sales',
            name='entryUser',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='daily_sales',
            name='updUser',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
