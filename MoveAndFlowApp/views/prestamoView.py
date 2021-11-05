from datetime import datetime
from django.db.models.query import QuerySet
from rest_framework import generics, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response


from MoveAndFlowApp.models.prestamo import Prestamo
from MoveAndFlowApp.models.bicicleta import Bicicleta
from MoveAndFlowApp.serializers import bicicletaSerializer
from MoveAndFlowApp.serializers.prestamoSerializer import PrestamoSerializer

import json


class PrestamoAllAndCreateView(generics.ListCreateAPIView):

    serializer_class = PrestamoSerializer

    def get_queryset(self):
        
        queryset = Prestamo.objects.all().order_by('p_id')
        return queryset

    def post(self, request, *args, **kwargs):
        
        origen_id = request.data["p_origen"]
        bicicletas = Bicicleta.objects.filter(
            b_en_estacion=origen_id).filter(b_condicion=True)
        if(len(bicicletas) == 0):
            return Response('No hay bicicletas disponibles para préstamos en la estación', status=status.HTTP_412_PRECONDITION_FAILED)
        else:
            request.data["p_bicicleta"] = bicicletas[0].b_id
            serializer = PrestamoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            bicicletas[0].b_en_prestamo = True

            #bicicletas[0].b_en_estacion = None
            
            print(str(vars(bicicletas[0])).split(",")[1:])
            bicicletas[0].save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PrestamoSingularView(generics.RetrieveUpdateDestroyAPIView):

    
    serializer_class = PrestamoSerializer

    queryset = Prestamo.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        
        def partial_update(request, *args, **kwargs):
            print('HOLA')

            kwargs['partial'] = True
            partial = kwargs.pop('partial', False)
            print(kwargs)

            bicicleta_id = self.get_object().p_bicicleta.b_id
            destino_id = self.get_object().p_destino.e_id



            instance = Bicicleta.objects.filter(b_id=bicicleta_id)[0]

            print(str(vars(instance)).split(",")[1:])

            instance.b_en_prestamo = True
            instance.b_en_estacion.e_id = 5

            print(instance.b_id)
            print(str(vars(instance)).split(",")[1:])
            instance.save()
            print(instance.b_id)
            print('CHAO')

            print(str(vars(instance)).split(",")[1:])
            #return Response(serializer.data, status=status.HTTP_200_OK)


        partial_update(self, request, *args, **kwargs)

        '''serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()'''
    

        return Response("Hola", status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        p_eliminado = self.get_object().p_id
        super().destroy(request, *args, **kwargs)
        return Response('Registro del préstamo con ID: ' + str(p_eliminado) + " eliminado con éxito del sistema.", status=status.HTTP_200_OK)


'''
Otra version de la clase PrestamoCreateView

class PrestamoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = PrestamoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(request.data)
'''
