from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

from .bicicleta import Bicicleta
from .estacion import Estacion

from datetime import datetime

class Prestamo(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_inicio = models.DateTimeField(auto_now_add=True)
    p_fin = models.DateTimeField(auto_now=True)
    p_bicicleta = models.ForeignKey(
        Bicicleta, related_name='presta', on_delete=SET_NULL, blank=True, null=True)
    p_origen = models.ForeignKey(
        Estacion, related_name='parte', on_delete=SET_NULL, blank=True, null=True)
    p_destino = models.ForeignKey(
        Estacion, related_name='llega', on_delete=SET_NULL, blank=True, null=True)
