# Generated by Django 4.1.1 on 2022-09-30 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hrms_users', '0002_alter_hrmsusers_managers_alter_hrmsusers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrmsusers',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
