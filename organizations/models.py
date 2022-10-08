from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Organization(models.Model):
    organization_name = models.CharField(max_length=200, unique=True)
    organization_tagline = models.TextField(max_length=300, null=True, blank=True)
    organization_vision = models.TextField(max_length=300, null=True, blank=True)
    organization_mission = models.CharField(max_length=200, null=True, blank=True)
    organization_logo = models.ImageField(null=True, blank=True, upload_to=upload_to, default='')
    organization_is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=200)
    established_date =  models.CharField(max_length=200, null=True, blank=True)
    organization_type = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class GroupHead(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    grouphead_type = models.CharField(max_length=200, null=True, blank=True)
    is_status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=500, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrganizationLocation(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=200)
    latitute = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitute = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    is_head_office = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrganizationDepartment(models.Model):
    grouphead_id = models.ForeignKey(GroupHead, on_delete=models.CASCADE, blank=True, null=True)
    department_title = models.CharField(max_length=200)
    department_description = models.TextField(max_length=500, null=True, blank=True)
    department_status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StaffClassification(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    technical_title = models.CharField(max_length=200, blank=True, null=True)
    non_technical_title = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    is_status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrganizationPosition(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True) 
    staff_id = models.ForeignKey(StaffClassification, on_delete=models.CASCADE, blank=True, null=True)
    position_title = models.CharField(max_length=200, null=True, blank=True)
    position_description = models.TextField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    department_status = models.BooleanField(default=True)
    salary_range = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    job_description = models.TextField(max_length=1000, null=True, blank=True)
    qualification_level = models.CharField(max_length=200, null=True, blank=True)
    user_experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


