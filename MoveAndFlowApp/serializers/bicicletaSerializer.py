from MoveAndFlowApp.models import Bicicleta
from rest_framework import serializers


class BicicletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicicleta
        fields = ['b_condicion', 'b_en_estacion']

        def create(self, validated_data):
            bicicletaInstance = Bicicleta.objects.create(**validated_data)
            return bicicletaInstance

        def to_representation(self, obj):
            bicicleta = Bicicleta.objects.get(b_id=obj.b_id)
            return {
                "b_id" : bicicleta.b_id,
                "b_condicion" : bicicleta.b_condicion,
                "b_en_estacion" : bicicleta.b_en_estacion
            }