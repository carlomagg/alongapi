from rest_framework import routers
from .api import BookridesViewSet

router = routers.DefaultRouter()
router.register('api/bookrides', BookridesViewSet, 'bookride')

urlpatterns = router.urls 