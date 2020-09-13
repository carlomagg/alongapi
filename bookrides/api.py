
from rest_framework import viewsets, permissions
from bookrides.models import Bookrides
from .serializers import BookridesSerializer

# Bookrides Viewset
class BookridesViewSet(viewsets.ModelViewSet):
    queryset = Bookrides.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookridesSerializer