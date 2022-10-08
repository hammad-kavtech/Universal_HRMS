from django.contrib import admin
from .models import Organization, GroupHead, OrganizationLocation, OrganizationDepartment, OrganizationPosition, StaffClassification
# Register your models here.

admin.site.register(Organization)
admin.site.register(GroupHead)
admin.site.register(OrganizationLocation)
admin.site.register(OrganizationDepartment)
admin.site.register(OrganizationPosition)
admin.site.register(StaffClassification)