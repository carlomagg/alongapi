from rest_framework import routers
from .api import UserrouteViewSet

router = routers.DefaultRouter()
router.register('api/userroute', UserrouteViewSet, 'userroute')

urlpatterns = router.urls 