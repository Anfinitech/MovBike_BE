from MoveAndFlowApp.models.prestamo import Prestamo
from rest_framework import serializers


class PrestamoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = ['p_inicio', 'p_origen', 'p_destino']


    def to_representation(self, obj):
        prestamo = Prestamo.objects.get(p_id=obj.p_id)
        return {
            "id" : prestamo.p_id,
            "inicio" : prestamo.p_inicio,
            "fin" : prestamo.p_fin,
            "origen" : prestamo.p_origen,
            "destino" : prestamo.p_destino,
        }