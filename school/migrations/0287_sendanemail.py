# Generated by Django 3.1.3 on 2021-05-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0286_center_branchname'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendanemail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(blank=True, max_length=255)),
                ('content', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]