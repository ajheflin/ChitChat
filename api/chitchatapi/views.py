from django.shortcuts import render
from chitchatapi.models import User, Chat
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chitchatapi.models import User
from .serializers import UserSerializer, ChatSerializer

class ListUsers(APIView):
    def get(self, reqeuest, format = None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)
class ListChats(APIView):
    def get(self, reqeuest, format = None):
        return Response(ChatSerializer(Chat.objects.all(), many=True).data)

# @api_view(["GET"])
# def index(request):


# Create your views here.
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()

