from django.urls import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Auto
import datetime

class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
     
        auto = 2
        a = Auto.objects.create(name='masda', summary='Prueba')
        with open('catalogo/static/images/logo.png', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

        for auto_id in range(auto):
            test_auto = Auto.objects.create(
                cabina=f'masda {auto_id}',
                summary=f'Prueba {auto_id}',
                url=f'Prueba.com {auto_id}',
                image= document
            )
            
            test_auto.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/autos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('autos'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('autos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'index.html')
        
