
from MoveAndFlowApp.models import Prestamo
from rest_framework import serializers


class PrestamoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prestamo
        fields = ['p_fin', 'p_bicicleta', 'p_origen', 'p_destino']

    def to_representation(self, obj):
        prestamo = Prestamo.objects.get(p_id=obj.p_id)
        return {
            "id": prestamo.p_id,
            "inicio": prestamo.p_inicio,
            "fin":  "Bici en Tránsito" if str(prestamo.p_fin)[:16] == str(prestamo.p_inicio)[:16] else prestamo.p_fin,
            'bici': prestamo.p_bicicleta.b_id,
            "origen": prestamo.p_origen.e_nombre,
            "destino": prestamo.p_destino.e_nombre,
        }
