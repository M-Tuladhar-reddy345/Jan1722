# Generated by Django 3.0.4 on 2021-07-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0353_extractplantdata_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='ver',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='extractplantdata',
            name='fileName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]