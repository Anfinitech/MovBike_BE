from rest_framework import generics, status
from rest_framework.response import Response

from MoveAndFlowApp.models.prestamo import Prestamo
from MoveAndFlowApp.serializers.prestamoSerializer import PrestamoSerializer

class PrestamoAllAndCreateView(generics.ListCreateAPIView):
    serializer_class = PrestamoSerializer

    def get_queryset(self):
        queryset = Prestamo.objects.all().order_by('p_inicio')
        return queryset
    
    def post(self, request, *args, **kwargs):
        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Prestamo creado exitosamente.', status=status.HTTP_201_CREATED)
    
    

class PrestamoSingularView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrestamoSerializer
    queryset = Prestamo.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return super().get(request,*args,**kwargs)


    def put(self, request, *args, **kwargs):
        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        p_eliminado = self.get_object().p_id
        super().destroy(request,*args,**kwargs)
        return Response('Prestamo con ID: ' + str(p_eliminado) + ", eliminado con éxito del sistema.", status=status.HTTP_200_OK)