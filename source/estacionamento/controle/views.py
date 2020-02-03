from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from estacionamento.controle.models import Parking
from estacionamento.controle.serializers import ParkingSerializer

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all().order_by('-arrival')
    serializer_class = ParkingSerializer

    @action(detail=True, methods=['put'])
    def pay(self, request, pk=None):
        parking_to_paid = self.get_object()
        serializer = ParkingSerializer
        if parking_to_paid:
            parking_to_paid.paid = True
            parking_to_paid.save()
            return Response({
                'id': parking_to_paid.id,
                'paid': True
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['put'])
    def out(self, request, pk=None):
        parking_to_out = self.get_object()
        serializer = ParkingSerializer
        if not parking_to_out.departure and parking_to_out.paid:
            parking_to_out.departure = timezone.now()
            parking_to_out.save()
            return Response({
                'id': parking_to_out.id,
                'departure': parking_to_out.departure
            })
        elif not parking_to_out.paid:
            return Response({
                'status': 'Necessita fazer o pagamento.'
            })
        else:
            return Response({
                'status': 'Veículo já partiu do estacionamento.'
            })
