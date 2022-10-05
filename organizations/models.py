from enum import unique
from django.db import models
from rest_framework import status

# Create your models here.
class organization(models.Model):
    organization_name = models.CharField(max_length=200, unique=True)
    organization_tagline = models.TextField(max_length=300, null=True, blank=True)
    organization_vision = models.TextField(max_length=300, null=True, blank=True)
    organization_mission = models.CharField(max_length=200, null=True, blank=True)
    organization_logo = models.ImageField(null=True, blank=True, upload_to='organization/', default='')
    organization_is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=200)
    established_date =  models.CharField(max_length=200, null=True, blank=True)
    company_type = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

