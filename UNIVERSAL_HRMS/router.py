from organizations.views import OrganizationViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewset, basename='organization')

urlpatterns = router.urls