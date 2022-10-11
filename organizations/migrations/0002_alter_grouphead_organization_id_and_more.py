# Generated by Django 4.1.1 on 2022-10-11 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouphead',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization'),
        ),
        migrations.AlterField(
            model_name='organizationdepartment',
            name='grouphead_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.grouphead'),
        ),
        migrations.AlterField(
            model_name='organizationlocation',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization'),
        ),
        migrations.AlterField(
            model_name='organizationposition',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organizationdepartment'),
        ),
        migrations.AlterField(
            model_name='organizationposition',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.staffclassification'),
        ),
        migrations.AlterField(
            model_name='staffclassification',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization'),
        ),
    ]