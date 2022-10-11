from django.db import models
from hrms_users.models import HrmsUsers
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Organization(models.Model):
    user_id = models.ForeignKey(HrmsUsers, on_delete=models.CASCADE, default=1)
    organization_name = models.CharField(max_length=200, unique=True)
    organization_tagline = models.TextField(max_length=300, null=True, blank=True)
    organization_vision = models.TextField(max_length=300, null=True, blank=True)
    organization_mission = models.CharField(max_length=200, null=True, blank=True)
    organization_logo = models.ImageField(null=True, blank=True, upload_to=upload_to, default='')
    organization_is_active = models.BooleanField(default=1)
    established_date =  models.CharField(max_length=200, null=True, blank=True)
    organization_type = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

grouphead_choices = (
    (1, 'Technical'),
    (2, 'Non-Technical'),
)

class GroupHead(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    grouphead_type = models.CharField(max_length=200, choices = grouphead_choices)
    is_status = models.BooleanField(default=1)
    is_active = models.BooleanField(default=1)
    description = models.TextField(max_length=500, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrganizationLocation(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=200)
    latitute = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitute = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    is_head_office = models.BooleanField(default=0)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrganizationDepartment(models.Model):
    grouphead_id = models.ForeignKey(GroupHead, on_delete=models.CASCADE)
    department_title = models.CharField(max_length=200)
    department_description = models.TextField(max_length=500, null=True, blank=True)
    department_status = models.BooleanField(default=1)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StaffClassification(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    technical_title = models.CharField(max_length=200, blank=True, null=True)
    non_technical_title = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, default="auto title")
    level = models.IntegerField(default=1)
    is_status = models.BooleanField(default=1)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrganizationPosition(models.Model):
    department_id = models.ForeignKey(OrganizationDepartment, on_delete=models.CASCADE) 
    staff_id = models.ForeignKey(StaffClassification, on_delete=models.CASCADE)
    position_title = models.CharField(max_length=200, null=True, blank=True)
    position_description = models.TextField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=1)
    department_status = models.BooleanField(default=1)
    salary_range = models.IntegerField(default=1, validators=[MaxValueValidator(100000000), MinValueValidator(1)])
    job_description = models.TextField(max_length=1000, null=True, blank=True)
    qualification_level = models.CharField(max_length=200, null=True, blank=True)
    user_experience = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





