from django.test import TestCase
from catalogo.models import Auto

class AutoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Auto.objects.create(nombre="masda")
            
    
    #def test_id() 

    def test_nombre_label(self):
        masda=Auto.objects.get(name="masda")
        field_label = auto._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')