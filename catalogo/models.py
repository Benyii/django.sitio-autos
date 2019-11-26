from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.conf import settings
from django_userforeignkey.models.fields import UserForeignKey
import uuid # Required for unique book instances
import datetime

User = get_user_model()


class Auto(models.Model):

	id = models.IntegerField(primary_key=True)
	autor = UserForeignKey(auto_user_add=True)
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
	imagen = models.ImageField(null=True)
	descripcion = models.TextField(max_length=1000, null=True, default='Vacio', help_text='Una breve descripcion')
	resena = models.TextField(max_length=1000, null=True, help_text='Explayate al describir sobre el vehiculo')
	valor = models.IntegerField(
		default='1',
		help_text='Valor del vehiculo en USD',
		validators=[
            MinValueValidator(1),
        ]
	)
	creado_en = models.DateTimeField(auto_now_add=True)
	modificado_el = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.nombre

class Comentario(models.Model):

	id = models.IntegerField(primary_key=True)
	autor = UserForeignKey(auto_user_add=True)
	post = models.ForeignKey(Auto, on_delete=models.CASCADE)
	comentario = models.TextField(max_length=1000, null=True)

	def __str__(self):
		return self.id






 
		

