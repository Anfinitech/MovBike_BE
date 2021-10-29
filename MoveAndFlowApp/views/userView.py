
from django.conf import settings

from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from MoveAndFlowApp.models import User
from MoveAndFlowApp.serializers.userSerializer import UserSerializer

@permission_classes([AllowAny])
class UserRegisterView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Usuario ' + request.data["username"] + ' creado exitosamente.', status=status.HTTP_201_CREATED)

class UserAllView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()   
    
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

class UserSingularView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(serializer.password)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):    
        u_eliminado = self.get_object().username
        super().destroy(request,*args,**kwargs)
        return Response(u_eliminado + " eliminado con éxito.", status=status.HTTP_200_OK)