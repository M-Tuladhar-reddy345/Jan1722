# Generated by Django 3.0.4 on 2021-11-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0440_auto_20211113_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='custserial',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]