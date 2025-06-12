from django.db import models
from clientes.models import Cliente
from repuestos.models import Repuesto  # Aseguramos importar Repuesto

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveSmallIntegerField()
    tipo = models.CharField(max_length=20)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    foto_frente = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    foto_trasera = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    foto_lateral1 = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    foto_lateral2 = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    fecha_proxima_revision = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.placa} ({self.marca} {self.modelo})"


class Mantenimiento(models.Model):
    TIPO_CHOICES = [
        ('PERIODO', 'Periódico'),
        ('REPARACION', 'Reparación'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_mantenimiento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha_mantenimiento = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Mantenimiento {self.tipo_mantenimiento} - {self.vehiculo}"


class RepuestoMantenimiento(models.Model):
    """
    Relaciona un Repuesto con un Mantenimiento.
    Necesario para el inline formset en Mantenimiento.
    """
    mantenimiento = models.ForeignKey(
        Mantenimiento,
        on_delete=models.CASCADE,
        related_name='repuestos'
    )
    repuesto = models.ForeignKey(
        Repuesto,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.repuesto} x{self.cantidad} para {self.mantenimiento}"
