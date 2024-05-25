from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import TestUserSerealizer, UserSerializer

#creacion de la funcion api_view
@api_view(['GET', 'POST'])
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        
        test_data = {
            'name': 'develop',
            'email': 'develop@gmail.com'
        }
        
        test_user = TestUserSerealizer(data = test_data)
        if test_user.is_valid():
            print("paso validacion")
        
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        #print(request.data)
        user_serializer = UserSerializer(data = request.data)
        #print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)  # Status code 201 for created
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)  # Status code 400 for bad request

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk = None):    
    user = User.objects.filter(id = pk).first()
    
    if user:
        #retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)        
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK) 
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #delete 
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'usuario eliminado correctamente'}, status = status.HTTP_204_NO_CONTENT)
    
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_404_NOT_FOUND)