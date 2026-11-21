from django.db import models

class Programa(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    facultad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre