from django.db import models

class Estacion(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_nombre = models.CharField(max_length=30,unique=True)
    e_estado = models.BooleanField(default=True)
    e_capacidad = models.IntegerField()