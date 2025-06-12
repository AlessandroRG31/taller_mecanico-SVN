from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dui = models.CharField(max_length=10, unique=True, verbose_name="DUI")
    telefono = models.CharField(max_length=9, blank=True, verbose_name="Teléfono")
    email = models.EmailField(blank=True, verbose_name="Email")
    direccion = models.TextField(blank=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
