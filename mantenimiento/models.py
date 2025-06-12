from django.db import models
from clientes.models import Cliente

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    tipo = models.CharField(max_length=30)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    foto_frente = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    foto_trasera = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    foto_lateral1 = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    foto_lateral2 = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    fecha_proxima_revision = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.placa} - {self.marca} {self.modelo}'

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_mantenimiento = models.CharField(max_length=50, choices=[
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
        # Agrega más si quieres
    ])
    fecha_mantenimiento = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Mantenimiento {self.tipo_mantenimiento} para {self.vehiculo.placa}'
