# Generated by Django 3.1.2 on 2021-02-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0230_auto_20210218_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('pin', models.IntegerField(blank=True, default=1, null=True)),
                ('contno', models.BigIntegerField(blank=True, default=1, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='remove',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
