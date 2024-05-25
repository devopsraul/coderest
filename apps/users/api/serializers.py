from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'#puede mencionar campo especidifcos con ['name', 'lastname',..]
        
class TestUserSerealizer(serializers.Serializer):       
    name = serializers.CharField(max_length = 255)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'developer' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        print(value)
        return value
    
    def validate_email(self, value):
        #custom validation
        if value == '':
            raise serializers.ValidationError('Tiene que indicar un correo')
        
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('el email no puede contener el nombre')
        
        return value
    
    def validate(self, data):
        return data 
    
    def create(self, validated_data):
        return User.objects.create (**validated_data)
    
    def update(self, instance, validate_data):
        #codigo interno que hace el serializers, por cada valors del modelo
        instance.name = validate_data.get('name', instance.name)
        instance.email = validate_data.get('email', instance.email)
        instance.save()
        print(instance)
        return instance