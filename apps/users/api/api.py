from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

#creacion de la funcion api_view
@api_view(['GET', 'POST'])
def user_api_view(request):
    
    #lista
    if request.method == 'GET':
        #queryset
        users = User.objects.all().values('id', 'username', 'email', 'password')
        #print (users)
        users_serializer = UserListSerializer(users, many = True)        
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        #print(request.data)
        user_serializer = UserSerializer(data = request.data)
        #print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            #return Response(user_serializer.data, status = status.HTTP_201_CREATED)  # Status code 201 for created
            return Response({'message': 'usuario creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)  # Status code 400 for bad request

#create
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
            user_serializer = UserSerializer(user, data = request.data, context = request.data)        
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK) 
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #delete 
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'usuario eliminado correctamente'}, status = status.HTTP_204_NO_CONTENT)
    
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_404_NOT_FOUND)