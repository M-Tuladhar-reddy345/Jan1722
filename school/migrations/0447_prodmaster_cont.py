# Generated by Django 3.0.4 on 2021-11-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0446_prodmaster_splcustcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodmaster',
            name='cont',
            field=models.CharField(blank=True, default='Pac', max_length=3, null=True),
        ),
    ]