from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from MoveAndFlowApp.models.estacion import Estacion
from MoveAndFlowApp.serializers.estacionSerializer import EstacionSerializer

class EstacionCreateView(generics.CreateAPIView):
    serializer_class = EstacionSerializer
    def post(self, request, *args, **kwargs):

        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        serializer = EstacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response("Creación exitosa", status=status.HTTP_201_CREATED)

class EstacionDetailView(generics.RetrieveAPIView):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

class EstacionesView(generics.ListAPIView):
    serializer_class = EstacionSerializer
    
    def get_queryset(self):
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        queryset = Estacion.objects.all() #.filter(b_en_estacion=self.kwargs['estacion'])
        return queryset

class EstacionUpdateView(generics.UpdateAPIView):
    serializer_class = EstacionSerializer
    queryset = Estacion.objects.all()

    def post(self, request, *args, **kwargs):

        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        serializer = EstacionSerializer(data=request.data['Estacion_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return super().update(request,*args,**kwargs)

class EstacionDeleteView(generics.DestroyAPIView):
    serializer_class = EstacionSerializer
    queryset = Estacion.objects.all()

    def post(self, request, *args, **kwargs):
        
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        serializer = EstacionSerializer(data=request.data['Estacion_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return super().destroy(request,*args,**kwargs)