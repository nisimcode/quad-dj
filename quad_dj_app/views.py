from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from quad_dj_app.models import Word


@api_view(['GET'])
def new_game(request):
    chosen = Word.objects.filter(is_deleted=False).order_by("?").first()

    lst = [chosen.l1, chosen.l2, chosen.l3, chosen.l4, chosen.l5]
    dct = {}
    for item in lst:
        if item not in dct:
            dct[item] = 0
        dct[item] += 1

    data = {
        'l1': chosen.l1,
        'l2': chosen.l2,
        'l3': chosen.l3,
        'l4': chosen.l4,
        'l5': chosen.l5,
        'dct': dct,
        'word': chosen.name
    }

    return Response(data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def signup(request):
#     User.objects.create_user(
#         username=request.data['username'],
#         first_name=request.data['first_name'],
#         last_name=request.data['last_name'],
#         email=request.data['email'],
#         password=request.data['password'])
#     return Response(status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET'])
# @authentication_classes([BasicAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def users(request):
#     if request.method == 'GET':
#         data = {
#             'username': request.user.username,
#             'userId': request.user.id
#         }
#         return Response(data)
#
#
# @api_view(['GET', 'PUT'])
# @authentication_classes([BasicAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def current_profile(request):
#     if request.method == 'GET':
#         data = {
#             'username': request.user.username,
#             'userId': request.user.id
#         }
#         return Response(data)
#
#     if request.method == 'PUT':
#         user = User.objects.get(pk=request.user.id)
#         user['first_name'] = request.data.first_name
#         user['last_name'] = request.data.last_name
#         user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)









