from organizations.views import OrganizationViewset, GroupHeadViewset, OrganizationDepartmentViewset, OrganizationPositionViewset, StaffClassificationViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewset, basename='organization')
router.register(r'organization/grouphead', GroupHeadViewset, basename='grouphead')
# router.register(r'organization/location', OrganizationLocationViewset, basename='organization_location')
router.register(r'organization/department', OrganizationDepartmentViewset, basename='organization_department')
router.register(r'organization/position', OrganizationPositionViewset, basename='organization_position')
router.register(r'organization/staff_classification', StaffClassificationViewset, basename='staff_classification')

urlpatterns = router.urls