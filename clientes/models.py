from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dui = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
