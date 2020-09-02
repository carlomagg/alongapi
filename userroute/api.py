from rest_framework import viewsets, permissions
from userroute.models import Userroute
from .serializers import UserrouteSerializer

# Driver Viewset
class UserrouteViewSet(viewsets.ModelViewSet):
    queryset = Userroute.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserrouteSerializer