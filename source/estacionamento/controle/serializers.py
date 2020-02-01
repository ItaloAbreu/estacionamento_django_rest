from rest_framework import serializers
from .models import Parking

class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = [
			'license_plate',
			'reservation_number',
			'arrival',
			'departure'
        ]