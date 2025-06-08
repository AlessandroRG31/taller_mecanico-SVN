from django.db import models
from django.core.validators import RegexValidator

class Cliente(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    dui = models.CharField(
        "DUI",
        max_length=9,
        unique=True,
        validators=[RegexValidator(r'^\d{7}-\d$', "Formato: 1234567-8")]
    )
    licencia_conducir = models.CharField(
        "Licencia de conducir",
        max_length=30,
        blank=True,
        null=True
    )
    licencia_circulacion = models.CharField(
        "Licencia de circulación",
        max_length=30,
        blank=True,
        null=True
    )
    telefono = models.CharField(
        "Teléfono",
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', "Debe contener 8 dígitos")]
    )
    direccion = models.TextField("Dirección")

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dui})"
