# Generated by Django 3.0.4 on 2021-10-17 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0419_alter_coupon_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodmaster',
            old_name='custCode',
            new_name='custType',
        ),
    ]
