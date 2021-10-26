from rest_framework import generics, status
from rest_framework.response import Response

from MoveAndFlowApp.models.bicicleta import Bicicleta
from MoveAndFlowApp.serializers.bicicletaSerializer import BicicletaSerializer

class BicicletaAllAndCreateView(generics.ListCreateAPIView):
    serializer_class = BicicletaSerializer

    def get_queryset(self):
        queryset = Bicicleta.objects.all().order_by('b_en_estacion')
        return queryset
    
    def post(self, request, *args, **kwargs):
        serializer = BicicletaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Bicicleta creada exitosamente.', status=status.HTTP_201_CREATED)
    
    

class BicicletaSingularView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BicicletaSerializer
    queryset = Bicicleta.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return super().get(request,*args,**kwargs)


    def put(self, request, *args, **kwargs):
        serializer = BicicletaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        b_eliminada = self.get_object()
        b_eliminada_en = self.get_object().b_en_estacion
        super().destroy(request,*args,**kwargs)
        return Response(status=status.HTTP_200_OK)


'''
Otra version de la clase BicicletaCreateView

class BicicletaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = BicicletaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(request.data)
'''