# Generated by Django 3.2 on 2021-10-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0420_auto_20211017_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='active',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
