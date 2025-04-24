from django.db import models

class Empresa(models.Model):
    nombre   = models.CharField("Nombre", max_length=100)
    direccion= models.CharField("Dirección", max_length=200)
    telefono = models.CharField("Teléfono", max_length=20, blank=True, null=True)  # <- aquí añadimos blank & null
    # resto de campos…
