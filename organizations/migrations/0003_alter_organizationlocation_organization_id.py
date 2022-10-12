# Generated by Django 4.1.1 on 2022-10-12 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_alter_grouphead_is_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationlocation',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='organizations.organization'),
        ),
    ]
