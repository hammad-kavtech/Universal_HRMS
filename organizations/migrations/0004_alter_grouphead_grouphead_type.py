# Generated by Django 4.1.1 on 2022-10-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_organizationposition_user_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouphead',
            name='grouphead_type',
            field=models.CharField(choices=[(1, 'Technical'), (2, 'Non-Technical')], max_length=200),
        ),
    ]
