from rest_framework import serializers
from bookrides.models import Bookrides

# Passenger Serializer
class BookridesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookrides
        fields = '__all__'