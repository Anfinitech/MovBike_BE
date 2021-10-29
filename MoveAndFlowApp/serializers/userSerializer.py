from rest_framework import serializers
from MoveAndFlowApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email', 'role']

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        print("Serializer: " + user.password)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'role': user.role
                }