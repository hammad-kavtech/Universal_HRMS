# Generated by Django 4.1.1 on 2022-10-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_alter_grouphead_organization_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationposition',
            name='user_experience',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
