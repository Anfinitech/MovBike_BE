from datetime import datetime
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from MoveAndFlowApp.models.prestamo import Prestamo
from MoveAndFlowApp.models.bicicleta import Bicicleta
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

            bicicletas[0].b_en_estacion = None
            print(str(vars(bicicletas[0])).split(",")[1:])
            bicicletas[0].save()

            return Response('Préstamo registrado exitosamente.', status=status.HTTP_201_CREATED)


class PrestamoSingularView(generics.RetrieveUpdateDestroyAPIView):

    
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):

        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   

        bicicleta_id = self.get_object().p_bicicleta.b_id
        bicicleta = Bicicleta.objects.filter(b_id=bicicleta_id)


        bicicleta[0].b_en_prestamo = False
        bicicleta[0].b_condicion = False
        destino_id = self.get_object().p_destino.e_id


        bicicleta[0].b_en_estacion.e_id = destino_id
        bicicleta[0].save()

        
        serializer.save()
        
        super().update(request, *args, **kwargs)

        return Response('La bici con ID: ' + str(bicicleta_id) + " ha llegado a " + destino_id + ".", status=status.HTTP_200_OK)

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
