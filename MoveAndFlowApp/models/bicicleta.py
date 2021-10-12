from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from.estacion import Estacion

class Bicicleta(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_condicion = models.BooleanField()
    b_en_prestamo = models.IntegerField(null=True)
    b_en_estacion = models.ForeignKey(Estacion, related_name='contiene', on_delete=CASCADE, blank=True, null=True)