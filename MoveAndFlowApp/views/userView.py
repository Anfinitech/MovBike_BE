
from django.conf import settings

from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from MoveAndFlowApp.models import User
from MoveAndFlowApp.serializers.userSerializer import UserSerializer

class UserRegisterView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class UserAllView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()   
    
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    