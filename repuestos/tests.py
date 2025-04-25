from django.test import TestCase
from django.urls  import reverse
from .models      import Empresa, Repuesto

class RepuestoSearchTestCase(TestCase):
    def setUp(self):
        emp = Empresa.objects.create(nombre='Taller Uno', telefono='123456')
        Repuesto.objects.create(empresa=emp, nombre='Filtro aceite', precio=50, stock=3)
        Repuesto.objects.create(empresa=emp, nombre='Filtro aire',  precio=30, stock=0)

    def test_search_returns_only_stock_gt_zero(self):
        res = self.client.get(reverse('repuestos:buscar_repuestos') + '?q=Filtro')
        self.assertContains(res, 'Filtro aceite')
        self.assertNotContains(res, 'Filtro aire')

    def test_order_by_price(self):
        emp = Empresa.objects.first()
        Repuesto.objects.create(empresa=emp, nombre='Filtro freno', precio=20, stock=5)
        res = self.client.get(reverse('repuestos:buscar_repuestos') + '?orden=precio')
        ct = res.content.decode()
        self.assertTrue(ct.index('Filtro freno') < ct.index('Filtro aceite'))
