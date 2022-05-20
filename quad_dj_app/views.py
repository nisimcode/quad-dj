from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view(['POST'])
def signup(request):
    User.objects.create_user(
        username=request.data['username'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email'],
        password=request.data['password'])
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    if request.method == 'GET':
        data = {
            'username': request.user.username,
            'userId': request.user.id
        }
        return Response(data)


@api_view(['GET', 'PUT'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_profile(request):
    if request.method == 'GET':
        data = {
            'username': request.user.username,
            'userId': request.user.id
        }
        return Response(data)

    if request.method == 'PUT':
        user = User.objects.get(pk=request.user.id)
        user['first_name'] = request.data.first_name
        user['last_name'] = request.data.last_name
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
