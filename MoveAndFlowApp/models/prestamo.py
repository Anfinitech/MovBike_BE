from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from.estacion import Estacion

class Prestamo(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_inicio = models.DateTimeField(auto_now_add=True)
    p_fin = models.DateTimeField()
    p_origen = models.ForeignKey(Estacion, related_name = 'presta', on_delete=CASCADE, blank=True)
    p_destino = models.ForeignKey(Estacion, related_name = 'recibe', on_delete=CASCADE, blank=True)