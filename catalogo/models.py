from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid # Required for unique book instances

class Auto(models.Model):

	nombre = models.CharField(max_length=200, default='Nombre vehiculo')
	cabina = models.IntegerField(
		default='1',
		help_text='Cantidad de asientos',
		validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
	)
	modelo = models.CharField(max_length=50, default='Modelo vehiculo')
	marca = models.CharField(max_length=50, default='Marca vehiculo')
	imagen = models.FileField(upload_to='catalogo/static/images/blog/', null=True)
	
	def __str__(self):
		return self.nombre

class Post(models.Model):

  	title = models.CharField(max_length=250)
  	body = models.TextField()
  	created_at = models.DateTimeField(auto_now_add=True)
  	updated_at = models.DateTimeField(auto_now=True)

 
		

