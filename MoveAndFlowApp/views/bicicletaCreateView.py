from rest_framework import status, views
from rest_framework.response import Response
from MoveAndFlowApp.serializers.bicicletaSerializer import BicicletaSerializer

class BicicletaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = BicicletaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(request.data)

