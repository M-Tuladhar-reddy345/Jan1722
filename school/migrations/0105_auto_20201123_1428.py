# Generated by Django 3.1.3 on 2020-11-23 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0104_auto_20201123_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='high_report',
            old_name='shift_loc',
            new_name='shift_loc1',
        ),
    ]