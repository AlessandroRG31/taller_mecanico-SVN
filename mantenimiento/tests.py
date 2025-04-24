# mantenimiento/tests.py
from django.test import TestCase
from .models import Vehiculo

class VehiculoModelTest(TestCase):
    def test_creacion_vehiculo(self):
        v = Vehiculo.objects.create(
            placa='ABC123', cliente='Juan'
        )
        self.assertEqual(v.placa, 'ABC123')
