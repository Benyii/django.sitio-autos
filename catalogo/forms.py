from django import forms

from .models import Auto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import copy
import datetime
import re
import warnings
from collections import defaultdict
from itertools import chain

from django.conf import settings
from django.forms.utils import to_current_timezone
from django.templatetags.static import static
from django.utils import datetime_safe, formats
from django.utils.datastructures import OrderedSet
from django.utils.dates import MONTHS
from django.utils.formats import get_format
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
from django.utils.topological_sort import (
    CyclicDependencyError, stable_topological_sort,
)
from django.utils.translation import gettext_lazy as _

class AutoForm(forms.ModelForm):

	class Meta:
		model = Auto

		fields = [
			'nombre',
			'cabina',
			'modelo',
			'marca',
			'descripcion',
			'resena',
			'imagen',
			'valor',
		]
		labels = {
			'nombre': 'Nombre',
			'cabina': 'Cabina',
			'modelo': 'Modelo',
			'marca': 'Marca',
			'descripcion': 'Descripcion',
			'resena': 'Reseña',
			'imagen': 'Imagen',
			'valor': 'Valor en USD',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'cabina': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center','type':'number'}),
			'modelo': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'marca': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'descripcion': forms.Textarea(attrs={'class': 'form-control', 'size': 100, 'type':'textarea'}),
			'resena': forms.Textarea(attrs={'class': 'form-control', 'size': 100, 'type':'textarea'}),
			'imagen': forms.FileInput(attrs={'class': 'form-control col-12 justify-content-center','type':'file'}),
			'valor': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center','type':'number'}),
		}

class AutoEditForm(forms.ModelForm):

	class Meta:
		model = Auto

		fields = [
			'cabina',
			'modelo',
			'marca',
			'descripcion',
			'resena',
			'valor',
		]
		labels = {
			'cabina': 'Cabina',
			'modelo': 'Modelo',
			'marca': 'Marca',
			'descripcion': 'Descripcion',
			'resena' : 'Reseña',
			'valor' : 'Valor en USD',
		}
		widgets = {
			'cabina': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center','type':'number'}),
			'modelo': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'marca': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center'}),
			'descripcion': forms.Textarea(attrs={'class': 'narrow-select form-control col-12 justify-content-center', 'size': 100}),
			'resena': forms.Textarea(attrs={'class': 'form-control', 'size': 100, 'type':'textarea'}),
			'valor': forms.TextInput(attrs={'class': 'form-control col-12 justify-content-center','type':'number'}),
		}
