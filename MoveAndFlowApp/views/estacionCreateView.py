from rest_framework import status, views
from rest_framework.response import Response
from MoveAndFlowApp.serializers.estacionSerializer import EstacionSerializer

'''
Esta vista efectivamente devuelve el JSON de la bici
pero en estacionView.py hay una clase con el mismo
nombre que hace lo mismo pero se escribe de manera diferente.

class EstacionCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = EstacionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Nice")
'''