# Generated by Django 3.1.3 on 2021-03-12 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0264_auto_20210312_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_dataa',
            name='updatedd_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='klupdatee', to=settings.AUTH_USER_MODEL),
        ),
    ]
