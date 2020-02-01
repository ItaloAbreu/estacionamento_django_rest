from rest_framework import viewsets
from estacionamento.controle.models import Parking
from estacionamento.controle.serializers import ParkingSerializer

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all().order_by('-arrival')
    serializer_class = ParkingSerializer