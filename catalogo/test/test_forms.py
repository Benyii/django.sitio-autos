from django.test import TestCase
from catalogo.forms import AutoForm, AutoEditForm
from catalogo.models import Auto
from django.core.files.uploadedfile import SimpleUploadedFile


class TestFormulario(TestCase):

    def setUp(self):
        with open('catalogo/static/images/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        self.auto = Auto.objects.create(
            nombre='Prueba',
            cabina=2,
            modelo='Prueba',
            marca='Prueba',
            descripcion='prueba',
            resena='descripcion',
            imagen=document,
            valor=100000)

    def test_AutoForm_valid(self):
        with open('catalogo/static/images/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')
            
        form = AutoForm(data={'nombre': "Prueba", 'cabina': 2, 'modelo': "Prueba", 'marca': "Prueba",'descripcion': "prueba", 'imagen': document, 'resena':"descripcion",'valor':100000})
        self.assertTrue(form.is_valid())        

