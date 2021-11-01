from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from.estacion import Estacion

class Bicicleta(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_condicion = models.BooleanField()
    b_en_prestamo = models.BooleanField(default=False, null=True)
    b_en_estacion = models.ForeignKey(Estacion, related_name = 'contiene', on_delete=SET_NULL, blank=True, null=True)