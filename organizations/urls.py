from django.contrib import admin
from django.urls import path
from .views import ViewOrganization, CreateOrganization, UpdateOrganization, DeleteOrganization

urlpatterns = [
    path('create_organization/', CreateOrganization.as_view(), name="create_organization"),
    path('update_organization/<pk>/', UpdateOrganization.as_view(), name="update_organization"),
    path('delete_organization/<pk>/', DeleteOrganization.as_view(), name="remove_organization"),
    path('view_organization/<pk>/', ViewOrganization.as_view(), name="view_organization"),
]