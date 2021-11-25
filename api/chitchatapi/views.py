from django.shortcuts import render
from chitchatapi.models import Message, User, Chat
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chitchatapi.models import User
from .serializers import MessageSerializer, UserSerializer, ChatSerializer
from rest_framework.viewsets import ModelViewSet


class ListUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)

class GetUserInfo(APIView):
    def get(self, request, format=None, UID=None):
        userid = self.kwargs['UID']
        return Response(UserSerializer(User.objects.filter(id=userid), many=True).data)

class ListChats(APIView):
    def get(self, request, format=None):
        return Response(ChatSerializer(Chat.objects.all(), many=True).data)

class ListChatsForUser(APIView):
    def get(self, request, format=None, UID=None):
        userid = self.kwargs['UID']
        return Response(ChatSerializer(Chat.objects.filter(users__in=[userid]), many=True).data)

class ListMessages(APIView):
    def get(self, request, format=None):
        return Response(MessageSerializer(Message.objects.all(), many=True).data)

class ListMessagesForChat(APIView):
    def get(self, request, format=None, Chat=None):
        chatno = self.kwargs['Chat']
        return Response(MessageSerializer(Message.objects.filter(chat_id=chatno), many=True).data)
    # def get(self, request, format=None):
    #     pass

class UserManage(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChatManage(APIView):
    # creating a new chat
    # deleting a chat
    # archiving a chat
    # creating a new message in a chat
    # deleting a message in a chat
    # Editing chats (could be a feature)
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def put(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request):
        serializer = ChatSerializer(data=request.data)

class MessageManage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListNotifications():
    pass
    # getting notifications (once user reads, delete)

    # class ListArchive(APIView):

    # @api_view(["GET"])
    # def index(request):

    # Create your views here.
    # class UserList(generics.ListAPIView):
        # queryset = User.objects.all()
