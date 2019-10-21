from django import forms

from .models import Auto, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AutoForm(forms.ModelForm):

	class Meta:
		model = Auto

		fields = [
			'nombre',
			'cabina',
			'modelo',
			'marca',
			'imagen',
		]
		labels = {
			'nombre': 'Nombre',
			'cabina': 'Cabina',
			'modelo': 'Modelo',
			'marca': 'Marca',
			'imagen': 'Imagen',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'cabina': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center','type':'number'}),
			'modelo': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'marca': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'imagen': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center','type':'file'}),

		}

"""
class RegistroForm(UserCreationForm):

	class Meta:
		model = User

		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		help_texts={
				'username': None,
		}
		labels = {
				'username': 'Nombre de Usuario',
				'first_name': 'Nombres',
				'last_name': 'Apellidos',
				'email': 'Correo Electronico',
		}
"""
