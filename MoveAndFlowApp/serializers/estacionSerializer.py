from MoveAndFlowApp.models import Estacion, Bicicleta
from rest_framework import serializers
from .bicicletaSerializer import BicicletaSerializer
from django.db.models.functions import Concat
from django.db.models import TextField


class EstacionSerializer(serializers.ModelSerializer):

    class Meta:    
        model = Estacion
        fields = ['e_nombre', 'e_estado', 'e_capacidad']


    def to_representation(self, obj):
        estacion = Estacion.objects.get(e_id=obj.e_id)
        return {
            "e_id" : estacion.e_id,
            "e_nombre" : estacion.e_nombre,
            "e_estado" : "Abierta" if estacion.e_estado else "Cerrada",
            "e_capacidad" : estacion.e_capacidad,
            "e_ocupacion" : round((Bicicleta.objects.filter(b_en_estacion=estacion.e_id).count()/estacion.e_capacidad),4),
            "e_bicicletasD" : Bicicleta.objects.filter(b_en_estacion=estacion.e_id).filter(b_condicion=True).count(),
            "e_bicicletasND" : Bicicleta.objects.filter(b_en_estacion=estacion.e_id).filter(b_condicion=False).count(),
            "e_bicicletasT" : Bicicleta.objects.filter(b_en_estacion=obj.e_id).count()
        }
