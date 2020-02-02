from django.db import models
from django.utils import timezone
from .validators import validate_plate

# Create your models here.
class Parking(models.Model):
	plate = models.CharField(
		max_length=8, validators=[validate_plate], verbose_name='Placa do Veículo')
	reservation =  models.CharField(
		max_length=9, verbose_name='Número da Reserva')
	arrival = models.DateTimeField(auto_now_add=True, verbose_name='Entrada')
	departure = models.DateTimeField(
		null=True, blank=True, verbose_name='Saída')

	def __str__(self):
		return f'{self.reservation} ({self.plate})'

	def make_reservation(self):
		last = Parking.objects.filter(arrival__gte=timezone.now().date()).last()
		prefix = 'RESV'

		if not last:
			return "{0}{1}".format(prefix, '001')

		current_number = last.reservation.replace(prefix, '')
		current_number = str(int(current_number) + 1)
		if len(current_number) < 3:
			current_number = ((3 - len(current_number)) * '0') + current_number

		return "{0}{1}".format(prefix, current_number.zfill(3))

	def save(self, *args, **kwargs):
		if not self.reservation:
			self.reservation = self.make_reservation()
		super(Parking, self).save(*args, **kwargs)