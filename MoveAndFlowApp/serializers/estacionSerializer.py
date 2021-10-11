from MoveAndFlowApp.models import Estacion, Bicicleta
from rest_framework import serializers
from .bicicletaSerializer import BicicletaSerializer

class EstacionSerializer(serializers.ModelSerializer):
    bicicleta = BicicletaSerializer()

    class Meta:
        model = Estacion
        fields = ['e_nombre', 'e_estado', 'e_capacidad','bicicleta']

        def create(self, validated_data):
            bicicletaData = validated_data.pop('bicicleta')
            estacionInstance = Estacion.objects.create(**validated_data)
            Bicicleta.objects.create(b_en_estacion = estacionInstance, **bicicletaData)
            return estacionInstance

        def to_representation(self, obj):
            estacion = Estacion.objects.get(e_id=obj.e_id)
            bicicleta = Bicicleta.objects.get(b_en_estacion=obj.e_id)
            return {
                "e_nombre" : estacion.e_nombre,
                "e_estado" : estacion.e_estado,
                "e_capacidad" : estacion.e_capacidad,
                "bicicleta" : {
                    "b_bicicleta" : bicicleta.b_id,
                    "b_condicion" : bicicleta.b_condicion,
                }
            }