# Generated by Django 3.0.4 on 2020-10-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0032_auto_20201008_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='minmaxfat',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minmaxfat',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]