# Generated by Django 3.1.2 on 2021-03-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0262_rpt_routewisebillabstract_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='minmaxfat',
            name='category1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
