# repuestos/tests.py
from django.test import TestCase
from .models import Empresa, Repuesto

class RepuestoSearchTest(TestCase):
    def setUp(self):
        e = Empresa.objects.create(nombre='Taller X', direccion='C/ Falsa 123')
        Repuesto.objects.create(nombre='Filtro', descripcion='Filtro aceite', precio=10, stock=5, empresa=e)

    def test_busqueda_orden(self):
        response = self.client.get('/repuestos/buscar/?q=Filtro')
        self.assertContains(response, 'Filtro')
