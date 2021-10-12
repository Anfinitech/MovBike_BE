from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response

from MoveAndFlowApp.models.bicicleta import Bicicleta
from MoveAndFlowApp.serializers.bicicletaSerializer import BicicletaSerializer


class BicicletaCreateView(generics.CreateAPIView):
    serializer_class = BicicletaSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = BicicletaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response("Creación exitosa", status=status.HTTP_201_CREATED)


class BicicletaDetailView(generics.RetrieveAPIView):
    serializer_class = BicicletaSerializer
    queryset = Bicicleta.objects.all()

    def get(self,request,*args,**kwargs):    
        return super().get(request,*args,**kwargs)

# Una vista que sería más apropiada plantearla desde EstacionExtraDetailView
class BicicletaEstacionView(generics.ListAPIView):
    serializer_class = BicicletaSerializer
    
    def get_queryset(self):

        queryset = Bicicleta.objects.filter(b_en_estacion=self.kwargs['estacion'])
        return queryset


class BicicletaUpdateView(generics.UpdateAPIView):
    serializer_class = BicicletaSerializer
    queryset = Bicicleta.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = BicicletaSerializer(data=request.data['bicicleta_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return super().update(request,*args,**kwargs)


class BicicletaDeleteView(generics.DestroyAPIView):
    serializer_class = BicicletaSerializer
    queryset = Bicicleta.objects.all()

    def post(self, request, *args, **kwargs):

        serializer = BicicletaSerializer(data=request.data['bicicleta_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return super().destroy(request,*args,**kwargs)

'''
Otra version de la clase BicicletaCreateView

class BicicletaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = BicicletaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(request.data)
'''