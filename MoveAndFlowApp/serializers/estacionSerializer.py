from MoveAndFlowApp.models import Estacion, Bicicleta
from rest_framework import serializers
from .bicicletaSerializer import BicicletaSerializer
from django.db.models.functions import Concat
from django.db.models import TextField


class EstacionSerializer(serializers.ModelSerializer):
    e_estado = serializers.SerializerMethodField()
    e_ocupacion = serializers.SerializerMethodField() 
    e_bicicletasD = serializers.SerializerMethodField() 
    e_bicicletasND = serializers.SerializerMethodField() 
    e_bicicletasT = serializers.SerializerMethodField()  

    class Meta:    
        model = Estacion
        #fields = '__all__'
        fields = ['e_id', 'e_nombre', 'e_estado', 'e_capacidad','e_ocupacion','e_bicicletasD','e_bicicletasND','e_bicicletasT']

        def create(self, validated_data):
            estacionInstance = Estacion.objects.create(**validated_data)
            return estacionInstance
        
        def to_representation(self, obj):
            estacion = Estacion.objects.get(e_id=obj.e_id)
            return {
                "e_id" : estacion.e_id,
                "e_nombre" : estacion.e_nombre,
                "e_estado" : estacion.e_estado,
                "e_capacidad" : estacion.e_capacidad,
            }  

    def get_e_estado(self,obj):
        return "Abierta" if obj.e_estado else "Cerrada"
    
    def get_e_ocupacion(self,obj):
        return round((Bicicleta.objects.filter(b_en_estacion=obj.e_id).count()/obj.e_capacidad),4)
    
    def get_e_bicicletasD(self,obj):
        return (Bicicleta.objects.filter(b_en_estacion=obj.e_id).filter(b_condicion=True).count())

    def get_e_bicicletasND(self,obj):
        return (Bicicleta.objects.filter(b_en_estacion=obj.e_id).filter(b_condicion=False).count())

    def get_e_bicicletasT(self,obj):
        return (Bicicleta.objects.filter(b_en_estacion=obj.e_id).count())



"""
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
"""