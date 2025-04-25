from django.db import models
from django.core.validators import MinValueValidator

class Empresa(models.Model):
    nombre = models.CharField("Nombre de la empresa", max_length=100, unique=True)
    telefono = models.CharField("Teléfono", max_length=20, blank=True)

    class Meta:
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="repuestos"
    )
    nombre = models.CharField("Nombre del repuesto", max_length=100)
    precio = models.DecimalField(
        "Precio (S/.)",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    stock = models.PositiveIntegerField(
        "Stock disponible",
        validators=[MinValueValidator(0)]
    )

    class Meta:
        unique_together = [["empresa", "nombre"]]
        ordering = ["precio"]

    def __str__(self):
        return f"{self.nombre} ({self.empresa.nombre})"
