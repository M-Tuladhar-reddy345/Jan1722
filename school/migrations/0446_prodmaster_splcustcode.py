# Generated by Django 3.0.4 on 2021-11-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0445_auto_20211116_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodmaster',
            name='splCustCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]