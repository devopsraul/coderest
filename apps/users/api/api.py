from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

#creacion de la funcion api_view
@api_view(['GET', 'POST'])
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    elif request.method == 'POST':
        #print(request.data)
        user_serializer = UserSerializer(data = request.data)
        #print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=200)  # Status code 201 for created
        return Response(user_serializer.errors, status=400)  # Status code 400 for bad request

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk = None):
    
    if request.method == 'GET':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    
    elif request.method == 'PUT':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=200) 
        return Response(user_serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response('Eliminado')