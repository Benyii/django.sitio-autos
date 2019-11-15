from django.test import TestCase
from catalogo.models import Auto

class AutoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Auto.objects.create(nombre="masda")

    def test_name_label(self):
        auto=Auto.objects.get(id=1)
        field_label = auto._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_summary_label(self):
        auto=Auto.objects.get(id=1)
        field_label = auto._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')
    
    def test_name_max_length(self):
        auto=Auto.objects.get(id=1)
        max_length = auto._meta.get_field('nombre').max_length
        self.assertEquals(max_length,200)
    
    def test_summary_max_length(self):
        auto=Auto.objects.get(id=1)
        max_length = auto._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,1000)
