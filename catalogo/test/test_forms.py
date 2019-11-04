from django.test import TestCase
from catalogo.forms import Auto


class TestFormulario(TestCase):

    def test_auto_form_valid_data(self):
        form = Auto(data={
        'cabina': 1,
        'modelo': 'masda3',
        'marca': 'masda'

        })

        self.assertTrue(form.is_valid())

    def test_auto_form_no_data(self):
        form = Auto(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

