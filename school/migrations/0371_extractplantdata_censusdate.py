# Generated by Django 3.0.4 on 2021-07-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0370_centermasterdataexcelupload_ifscexcelupload_tsratesexcelupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='extractplantdata',
            name='censusdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]