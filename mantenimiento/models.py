from django.db import models
from django.utils import timezone
from repuestos.models import Repuesto

class Vehiculo(models.Model):
    cliente         = models.CharField(max_length=100)
    placa           = models.CharField(max_length=20, unique=True)
    foto_placa      = models.ImageField(upload_to='vehiculos/placas/')
    marca           = models.CharField(max_length=50)
    modelo          = models.CharField(max_length=50)
    # Le añadimos default para evitar el prompt en makemigrations
    anio            = models.PositiveSmallIntegerField(default=timezone.now().year)
    tipo            = models.CharField(max_length=50)
    costo           = models.DecimalField(max_digits=10, decimal_places=2)
    foto_frente     = models.ImageField(upload_to='vehiculos/frente/', blank=True)
    foto_trasera    = models.ImageField(upload_to='vehiculos/trasera/', blank=True)
    foto_lateral1   = models.ImageField(upload_to='vehiculos/lateral1/', blank=True)
    foto_lateral2   = models.ImageField(upload_to='vehiculos/lateral2/', blank=True)

    def __str__(self):
        return f"{self.placa} – {self.cliente}"

class ProximoMantenimiento(models.Model):
    vehiculo         = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='proximos')
    fecha_programada = models.DateField()

    def __str__(self):
        return f"Próximo mant. {self.vehiculo.placa} el {self.fecha_programada}"

class Mantenimiento(models.Model):
    vehiculo             = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenimientos')
    tipo_mantenimiento   = models.CharField(max_length=100)
    fecha_mantenimiento  = models.DateField(default=timezone.now)
    repuestos            = models.ManyToManyField(Repuesto, blank=True)
    costo                = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo_mantenimiento} – {self.vehiculo.placa} ({self.fecha_mantenimiento})"
