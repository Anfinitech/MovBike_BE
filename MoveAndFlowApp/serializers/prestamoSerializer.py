from MoveAndFlowApp.models.prestamo import Prestamo
from rest_framework import serializers
import datetime

datetime.timedelta(hours=5)
datetime.timedelta(5)



class PrestamoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = ['p_fin', 'p_origen', 'p_destino']


    def to_representation(self, obj):
        prestamo = Prestamo.objects.get(p_id=obj.p_id)
        return {
            "id" : prestamo.p_id,
            "inicio" : prestamo.p_inicio - datetime.timedelta(hours=5),
            "fin" : prestamo.p_fin - datetime.timedelta(hours=5),
            "origen" : prestamo.p_origen.e_nombre,
            "destino" : prestamo.p_destino.e_nombre,
        }