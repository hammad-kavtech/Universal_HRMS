from organizations.views import OrganizationViewset, GroupHeadViewset, OrganizationLocationViewset, OrganizationDepartmentViewset, OrganizationPositionViewset, StaffClassificationViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewset, basename='organization')
router.register(r'grouphead', GroupHeadViewset, basename='grouphead')
router.register(r'organization_location', OrganizationLocationViewset, basename='organization_location')
router.register(r'organization_department', OrganizationDepartmentViewset, basename='organization_department')
router.register(r'organization_position', OrganizationPositionViewset, basename='organization_position')
router.register(r'staff_classification', StaffClassificationViewset, basename='staff_classification')

urlpatterns = router.urls