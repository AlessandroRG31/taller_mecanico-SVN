# repuestos/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Empresa, Repuesto

class RepuestoSearchTestCase(TestCase):
    def setUp(self):
        self.emp = Empresa.objects.create(nombre='Taller Uno', telefono='123456')
        self.rep1 = Repuesto.objects.create(
            empresa=self.emp, nombre='Filtro aceite', precio=50, stock=3
        )
        self.rep2 = Repuesto.objects.create(
            empresa=self.emp, nombre='Filtro aire', precio=30, stock=0
        )

    def test_search_returns_only_stock_gt_zero(self):
        url = reverse('repuestos:buscar_repuestos') + '?q=Filtro'
        response = self.client.get(url)
        self.assertContains(response, 'Filtro aceite')
        self.assertNotContains(response, 'Filtro aire')

    def test_order_by_price(self):
        Repuesto.objects.create(
            empresa=self.emp, nombre='Filtro freno', precio=20, stock=5
        )
        url = reverse('repuestos:buscar_repuestos') + '?orden=precio'
        response = self.client.get(url)
        content = response.content.decode()
        self.assertTrue(content.index('Filtro freno') < content.index('Filtro aceite'))
