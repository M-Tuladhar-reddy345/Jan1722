# Generated by Django 3.0.4 on 2021-12-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0458_auto_20211210_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_sales',
            name='PAmt',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]