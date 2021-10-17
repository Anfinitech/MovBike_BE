from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from MoveAndFlowApp.models.estacion import Estacion
from MoveAndFlowApp.serializers.estacionSerializer import EstacionSerializer

@permission_classes([AllowAny])
class EstacionAllAndCreateView(generics.ListCreateAPIView):
    serializer_class = EstacionSerializer
    
    def get_queryset(self):
        queryset = Estacion.objects.all().order_by('e_id')
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = EstacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data['e_nombre'] + " creada con éxito.", status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class EstacionSingularView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EstacionSerializer
    queryset = Estacion.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        serializer = EstacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):    
        e_eliminada = self.get_object().e_nombre
        super().destroy(request,*args,**kwargs)
        return Response(e_eliminada + " eliminada con éxito.", status=status.HTTP_200_OK)

   

'''
Otra version de la clase EstacionCreateView

class EstacionCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = EstacionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Nice")
'''