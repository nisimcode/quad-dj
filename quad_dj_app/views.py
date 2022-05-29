from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from quad_dj_app.models import Word, Vocab, Note


@api_view(['GET'])
def vocabulary(request):
    vocab_objs = Vocab.objects.filter(is_deleted=False)
    vocab = []
    for obj in vocab_objs:
        vocab.append(obj.name)

    return Response(vocab, status=status.HTTP_200_OK)


@api_view(['POST'])
def notes(request):
    Note.objects.create(
        # user_id=request.data['user'],
        info=request.data['info'] if len(request.data['info']) else "",
        text=request.data['text'],
        spam=(len(set(request.data['text'])) < 3) or (len(request.data['text']) < 10)
    )
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def new_game(request):
    chosen = Word.objects.filter(is_deleted=False).order_by("?").first()
    ltr1, ltr2, ltr3, ltr4, ltr5 = chosen.l1, chosen.l2, chosen.l3, chosen.l4, chosen.l5
    if request.method == 'GET':

        lst = [ltr1, ltr2, ltr3, ltr4, ltr5]
        dct = {}
        for item in lst:
            if item not in dct:
                dct[item] = 0
            dct[item] += 1

        data = {
            'ltr1': ltr1,
            'ltr2': ltr2,
            'ltr3': ltr3,
            'ltr4': ltr4,
            'ltr5': ltr5,
            'dct': dct,
            'word': chosen.name,
            'def': chosen.definition
        }

        return Response(data, status=status.HTTP_200_OK)

    # elif request.method == 'POST':
    #     plc1, plc2, plc3, plc4, plc5 = \
    #         request.data.plc1, request.data.plc2, request.data.plc3, request.data.plc4, request.data.plc5
    #
    #     if not (plc1.isalpha() and
    #             plc2.isalpha() and
    #             plc3.isalpha() and
    #             plc4.isalpha() and
    #             plc5.isalpha()):
    #
    #         return Response("Enter letters only", status=status.HTTP_400_BAD_REQUEST)
    #
    #     user_word = ("".join([plc1, plc2, plc3, plc4, plc5])).lower()
    #
    #     if not(Vocab.objects.get(name=user_word)):
    #         return Response("Word not in dictionary", status=status.HTTP_400_BAD_REQUEST)
    #
    #     for






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









