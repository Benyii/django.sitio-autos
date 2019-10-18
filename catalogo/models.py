from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid # Required for unique book instances

class Auto(models.Model):
	nombre = models.CharField(max_length=200)

	cabina = models.IntegerField(
		default='1',
		help_text='Cantidad de asientos',
		validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
	)

	modelo = models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	imagen = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre