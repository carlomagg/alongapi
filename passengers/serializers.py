from rest_framework import serializers
from passengers.models import Passenger

# Passenger Serializer
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'