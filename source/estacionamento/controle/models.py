from django.db import models

# Create your models here.
class Parking(models.Model):
	license_plate = models.CharField(max_length=7)
	reservation_number = models.CharField(max_length=7)
	arrival = models.DateField()
	departure = models.DateField()

	def __str__(self):
		return f'{self.reservation_number} ({self.license_plate})'