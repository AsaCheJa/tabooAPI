#from collections import UserList
from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView 
from .serializers import CreateUserSerializer
#from .serializers import UserSerializer
#from rest_framework.decorators import api_view # original
from .models import User
#from apitaboo import serializers   # original

class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes =[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raize_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        token = Token.objects.create(user=serializer.instance)    
        token_data = {"token": token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )                        
class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
 

# Create your views here.
# @api_view (['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/user-list/',
#         'Datail View':'/user-detail/<str:pk>/',
#         'Create':'/user-create/',
#         'Update':'/user-update/<str:pk>/',
#         'Delete':'/user-delete/<str:pk>/',
#     }
#     return Response(api_urls)

# @api_view (['GET'])    
# def userList(request):
#     user = User.objects.all().order_by('-id')
#     serializer = UserSerializer(user, many=True)
#     return Response(serializer.data)

# @api_view (['GET'])
# def userDetail(request, pk):
# 	user = User.objects.get(id=pk)
# 	serializer = UserSerializer(user, many=False)
# 	return Response(serializer.data)

# @api_view(['POST'])
# def userCreate(request):
# 	serializer = UserSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['POST'])
# def userUpdate(request, pk):
# 	user = User.objects.get(id=pk)
# 	serializer = UserSerializer(instance=user, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)


# @api_view(['DELETE'])
# def userDelete(request, pk):
# 	user = User.objects.get(id=pk)
# 	user.delete()

# 	return Response('Item succsesfully delete!')