from rest_framework import viewsets, permissions
from drivers.models import Driver
from .serializers import DriverSerializer

# Driver Viewset
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DriverSerializer