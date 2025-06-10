from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from repuestos.models import Repuesto
from clientes.models import Cliente
from datetime import timedelta

class Vehiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        verbose_name="Cliente",
        on_delete=models.CASCADE,
        related_name="vehiculos"
    )
    placa = models.CharField("Placa", max_length=20, unique=True)
    marca = models.CharField("Marca", max_length=50, blank=True, default='')
    modelo = models.CharField("Modelo", max_length=50, blank=True, default='')
    anio = models.PositiveSmallIntegerField("Año", default=timezone.now().year)
    tipo = models.CharField("Tipo de vehículo", max_length=50, blank=True, default='')
    costo = models.DecimalField(
        "Costo (S/.)", max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)], default=0.0
    )
    foto_placa = models.ImageField(
        "Foto de la placa", upload_to='vehiculos/placas/',
        blank=True, null=True
    )
    foto_frente = models.ImageField(
        "Foto frontal", upload_to='vehiculos/frente/',
        blank=True, null=True
    )
    foto_trasera = models.ImageField(
        "Foto trasera", upload_to='vehiculos/trasera/',
        blank=True, null=True
    )
    foto_lateral1 = models.ImageField(
        "Foto lateral 1", upload_to='vehiculos/lateral1/',
        blank=True, null=True
    )
    foto_lateral2 = models.ImageField(
        "Foto lateral 2", upload_to='vehiculos/lateral2/',
        blank=True, null=True
    )
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_proxima_revision = models.DateField(blank=True, null=True)

    def calcular_fecha_proxima(self, dias_intervalo=180):
        base = self.fecha_proxima_revision or self.fecha_registro or timezone.now().date()
        self.fecha_proxima_revision = base + timedelta(days=dias_intervalo)
        return self.fecha_proxima_revision

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Primero guarda para asegurar fecha_registro
        if not self.fecha_proxima_revision:
            self.calcular_fecha_proxima()
            super().save(update_fields=["fecha_proxima_revision"])

    def __str__(self):
        return f"{self.placa} – {self.cliente}"

class ProximoMantenimiento(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, related_name='proximos'
    )
    fecha_programada = models.DateField("Fecha programada")

    def __str__(self):
        return f"Próximo mant. {self.vehiculo.placa} el {self.fecha_programada}"

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, related_name='mantenimientos'
    )
    tipo_mantenimiento = models.CharField(
        "Tipo de mantenimiento", max_length=100, blank=True, default=''
    )
    fecha_mantenimiento = models.DateField("Fecha", default=timezone.now)
    repuestos = models.ManyToManyField(
        Repuesto,
        through='RepuestoMantenimiento',
        blank=True,
        related_name='mantenimientos'
    )
    costo = models.DecimalField(
        "Costo (S/.)", max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)], default=0.0
    )

    def __str__(self):
        return f"{self.tipo_mantenimiento} – {self.vehiculo.placa} ({self.fecha_mantenimiento})"

class RepuestoMantenimiento(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(
        "Cantidad",
        validators=[MinValueValidator(1)],
        default=1
    )

    def __str__(self):
        return f"{self.cantidad}× {self.repuesto.nombre} en mant. {self.mantenimiento.id}"
