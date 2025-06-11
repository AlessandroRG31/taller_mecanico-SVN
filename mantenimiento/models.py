from django.db import models
from django.core.validators import MinValueValidator
from repuestos.models import Repuesto
from clientes.models import Cliente

class Vehiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="vehiculos",
        verbose_name="Cliente"
    )
    placa = models.CharField("Placa", max_length=20, unique=True)
    marca = models.CharField("Marca", max_length=50)
    modelo = models.CharField("Modelo", max_length=50)
    anio = models.PositiveIntegerField("Año", validators=[MinValueValidator(1886)])
    tipo = models.CharField("Tipo", max_length=30)
    costo = models.DecimalField("Costo", max_digits=10, decimal_places=2)
    foto_frente = models.ImageField("Foto frontal", upload_to="vehiculos/%Y/%m/%d/", blank=True, null=True)
    foto_trasera = models.ImageField("Foto trasera", upload_to="vehiculos/%Y/%m/%d/", blank=True, null=True)
    foto_lateral1 = models.ImageField("Foto lateral 1", upload_to="vehiculos/%Y/%m/%d/", blank=True, null=True)
    foto_lateral2 = models.ImageField("Foto lateral 2", upload_to="vehiculos/%Y/%m/%d/", blank=True, null=True)
    fecha_proxima_revision = models.DateField("Próxima revisión", blank=True, null=True)

    def __str__(self):
        return f"{self.placa} – {self.marca} {self.modelo}"

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="mantenimientos")
    fecha_mantenimiento = models.DateField("Fecha de mantenimiento")
    costo = models.DecimalField("Costo", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Mantenimiento {self.id} – Vehículo {self.vehiculo.placa}"

class RepuestoMantenimiento(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE, related_name="repuestos")
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField("Cantidad", validators=[MinValueValidator(1)], default=1)

    def __str__(self):
        return f"{self.cantidad}× {self.repuesto.nombre} en Mantenimiento {self.mantenimiento.id}"
