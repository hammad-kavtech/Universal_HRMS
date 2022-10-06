from django.db import models

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
    company_type = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupHead(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True, blank=True)
    is_status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=500, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

