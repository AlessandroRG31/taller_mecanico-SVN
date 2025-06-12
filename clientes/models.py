from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dui = models.CharField("DUI", max_length=10, unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombre} – {self.dui}"
