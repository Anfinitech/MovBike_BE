from MoveAndFlowApp.models import Bicicleta
from rest_framework import serializers


class BicicletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicicleta
        fields = ['b_condicion']

