from django.shortcuts import render
from chitchatapi.models import User, Chat
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chitchatapi.models import User
from .serializers import UserSerializer, ChatSerializer


class ListUsers(APIView):
    def get(self, reqeuest, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)


class ListChats(APIView):
    def get(self, request, format=None):
        return Response(ChatSerializer(Chat.objects.all(), many=True).data)


# class ListMessages(APIView):
#     def get(self, request, format):


class ChatManage():
    # creating a new chat
    # deleting a chat
    # archiving a chat
    # creating a new message in a chat
    # deleting a message in a chat
    # Editing chats (could be a feature)
    def get(self):
        pass


class ListNotifications():
    # getting notifications (once user reads, delete)

    # class ListArchive(APIView):

    # @api_view(["GET"])
    # def index(request):

    # Create your views here.
    # class UserList(generics.ListAPIView):
    #     queryset = User.objects.all()
