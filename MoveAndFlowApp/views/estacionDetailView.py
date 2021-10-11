from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from MoveAndFlowApp.models.estacion import Estacion
from MoveAndFlowApp.serializers.estacionSerializer import EstacionSerializer

class EstacionDetailView(generics.RetrieveAPIView):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)