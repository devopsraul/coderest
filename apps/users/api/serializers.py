from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'#puede mencionar campo especificos con ('name', 'lastname',..)
        
    def to_representation(self, instance):
        #data = super().to_representation(instance)
        #print(data)
        return {
            'id': instance['id'],
            'nombre_usuario': instance['username'],
            'correo': instance['email'],
            'clave': instance['password'],
        }