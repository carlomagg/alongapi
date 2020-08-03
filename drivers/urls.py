from rest_framework import routers
from .api import DriverViewSet

router = routers.DefaultRouter()
router.register('api/drivers', DriverViewSet, 'drivers')

urlpatterns = router.urls               