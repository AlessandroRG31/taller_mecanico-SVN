# Ruta: taller_mecanico/mantenimiento/models.py

from django.db import models

class Vehiculo(models.Model):
    cliente = models.CharField("Cliente", max_length=100)
    placa = models.CharField("Placa", max_length=20, unique=True)
    foto_placa = models.ImageField("Foto de placa", upload_to='vehiculos/placas/', blank=True, null=True)
    marca = models.CharField("Marca", max_length=50, blank=True, null=True)
    modelo = models.CharField("Modelo", max_length=50, blank=True, null=True)
    anio = models.PositiveIntegerField("Año", blank=True, null=True)
    tipo = models.CharField("Tipo de vehículo", max_length=50, blank=True, null=True)
    costo = models.DecimalField("Costo de registro", max_digits=10, decimal_places=2, blank=True, null=True)
    foto_frente = models.ImageField("Foto frontal", upload_to='vehiculos/', blank=True, null=True)
    foto_trasera = models.ImageField("Foto trasera", upload_to='vehiculos/', blank=True, null=True)
    foto_lateral1 = models.ImageField("Foto costado A", upload_to='vehiculos/', blank=True, null=True)
    foto_lateral2 = models.ImageField("Foto costado B", upload_to='vehiculos/', blank=True, null=True)

    def __str__(self):
        return f"{self.placa} – {self.cliente}"

class ProximoMantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='proximos')
    fecha_programada = models.DateField("Fecha prevista de mantenimiento")

    class Meta:
        verbose_name = "Próximo mantenimiento"
        verbose_name_plural = "Próximos mantenimientos"

    def __str__(self):
        return f"{self.vehiculo.placa} → {self.fecha_programada}"

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenimientos')
    tipo_mantenimiento = models.CharField("Tipo mantenimiento", max_length=50)
    fecha_mantenimiento = models.DateField("Fecha del mantenimiento")
    repuestos = models.ManyToManyField('repuestos.Repuesto', verbose_name="Repuestos usados", blank=True)
    costo = models.DecimalField("Costo del mantenimiento", max_digits=10, decimal_places=2)

    def __str__(self):
       
        return f"{self.vehiculo.placa} – {self.tipo_mantenimiento} ({self.fecha_mantenimiento})"
