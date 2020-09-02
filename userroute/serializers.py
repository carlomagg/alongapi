from rest_framework import serializers
from userroute.models import Userroute

# Userroute Serializer
class UserrouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userroute
        fields = '__all__'