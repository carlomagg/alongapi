from rest_framework import routers
from .api import PassengerViewSet

router = routers.DefaultRouter()
router.register('api/passengers', PassengerViewSet, 'passenger')

urlpatterns = router.urls 