# Generated by Django 3.1.2 on 2021-03-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0260_auto_20210302_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_routewisebillabstract',
            name='aarrears',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
