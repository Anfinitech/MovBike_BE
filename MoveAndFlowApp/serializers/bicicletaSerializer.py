from MoveAndFlowApp.models import Bicicleta
from rest_framework import serializers


class BicicletaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bicicleta
        fields = ['b_condicion', 'b_en_estacion']


    def to_representation(self, obj):
        bicicleta = Bicicleta.objects.get(b_id=obj.b_id)
        return {
            "b_id" : bicicleta.b_id,
            "b_condicion" : "En buen estado" if bicicleta.b_condicion else "Averiada",
            "b_en_estacion" : bicicleta.b_en_estacion.e_nombre,
        }