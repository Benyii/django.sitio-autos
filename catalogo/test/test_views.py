from django.urls import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from catalogo.models import Auto
import datetime
from datetime import date

class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
     
        auto = 100
        with open('catalogo/static/images/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        test_auto = Auto.objects.create(
            nombre='Prueba',
            cabina=2,
            modelo='Prueba',
            marca='Prueba',
            imagen= document,
            descripcion='prueba',
            resena='descripcion',
            valor=100000)
            
        test_auto.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/blog')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        
        
