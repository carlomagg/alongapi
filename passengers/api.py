from rest_framework import viewsets, permissions
from passengers.models import Passenger
from .serializers import PassengerSerializer

# Driver Viewset
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PassengerSerializer