from django.urls import path 
from apps.users.api.api import UserAPIView

urlpaterns = [
    path('usuario/',UserAPIView.as_view(), name = 'usuario_api')
]