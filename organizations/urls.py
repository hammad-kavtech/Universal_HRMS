from django.contrib import admin
from django.urls import path
from .views import ViewOrganization, CreateOrganization, UpdateOrganization, ViewAllOrganizations, DeactivateOrganization, ViewActivateOrganization, ViewDeactivateOrganization

urlpatterns = [
    path('create_organization/', CreateOrganization.as_view(), name="create_organization"),
    path('update_organization/<pk>/', UpdateOrganization.as_view(), name="update_organization"),
    path('view_organization/<pk>/', ViewOrganization.as_view(), name="view_organization"),
    path('deactivate_organization/<pk>/', DeactivateOrganization.as_view(), name="deactivate_organization"),
   #path('get_organization/<pk>/', DeactivateOrganization.as_view(), name="deactivate_organization"),
    path('view_all_organization/', ViewAllOrganizations.as_view(), name="view_all_organization"),
    path('view_activate_organization/', ViewActivateOrganization.as_view(), name="view_activate_organization"),
    path('view_deactivate_organization/', ViewDeactivateOrganization.as_view(), name="view_deactivate_organization"),
]