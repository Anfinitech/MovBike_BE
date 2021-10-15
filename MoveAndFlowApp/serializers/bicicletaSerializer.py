from MoveAndFlowApp.models import Bicicleta
from rest_framework import serializers


class BicicletaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bicicleta
        fields = ['b_condicion', 'b_en_estacion']


    def to_representation(self, obj):
        bicicleta = Bicicleta.objects.get(b_id=obj.b_id)
        return {
            "id" : bicicleta.b_id,
            "condicion" : "En buen estado" if bicicleta.b_condicion else "Averiada",
            "estación_id" : bicicleta.b_en_estacion.e_id,
            "estacion_nombre" : bicicleta.b_en_estacion.e_nombre,
        }