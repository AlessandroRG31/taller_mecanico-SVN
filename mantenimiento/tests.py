# mantenimiento/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Vehiculo, ProximoMantenimiento, Mantenimiento
import datetime

class VehiculoTestCase(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            cliente='Juan Pérez', placa='ABC123', costo=1000
        )

    def test_vehiculo_str(self):
        self.assertEqual(str(self.vehiculo), 'ABC123 – Juan Pérez')

    def test_placa_unica(self):
        with self.assertRaises(Exception):
            Vehiculo.objects.create(cliente='Otro', placa='ABC123', costo=500)

class MantenimientoTestCase(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            cliente='Test', placa='XYZ789', costo=500
        )
        self.prox = ProximoMantenimiento.objects.create(
            vehiculo=self.vehiculo,
            fecha_programada=datetime.date.today() + datetime.timedelta(days=30)
        )

    def test_proximo_str(self):
        texto = str(self.prox)
        self.assertIn(self.vehiculo.placa, texto)

    def test_mantenimiento_create(self):
        mant = Mantenimiento.objects.create(
            vehiculo=self.vehiculo,
            tipo_mantenimiento='Cambio aceite',
            fecha_mantenimiento=datetime.date.today(),
            costo=200
        )
        self.assertIn(mant, self.vehiculo.mantenimientos.all())
