from rest_framework import status, views
from rest_framework.response import Response
from MoveAndFlowApp.serializers.estacionSerializer import EstacionSerializer

class EstacionCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = EstacionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Nice")
