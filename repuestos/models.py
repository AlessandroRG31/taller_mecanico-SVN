# taller_mecanico/repuestos/models.py
from django.db import models
class Empresa(models.Model):
    nombre   = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)  
    

class Repuesto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.empresa})"
