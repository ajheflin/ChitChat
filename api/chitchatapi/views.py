from django.shortcuts import render
from chitchatapi.models import Message, User, Chat
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chitchatapi.models import User
from .serializers import MessageSerializer, UserSerializer, ChatSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Chat as ChatModel, User as UserModel


# Takes a GET request with no parameters, returns a list of all users
class ListUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)

# Takes a GET request with ID in URL path, returns user info for given ID, see urls.py for more documentation.


class GetUserInfo(APIView):
    def get(self, request, format=None, UID=None):
        userid = self.kwargs['UID']
        return Response(UserSerializer(User.objects.filter(id=userid), many=True).data)

# Takes a GET request with username in URL path, returns user info for given username, see urls.py for more documentation.


class GetUserInfoByUsername(APIView):
    def get(self, request, format=None, username=None):
        username = self.kwargs['username']
        return Response(UserSerializer(User.objects.filter(username=username), many=True).data)


# Authenticates a user via a POST request, returns an object if the user/password combo is valid, or a 401 UNAUTHORIZED if the user/password combo is not valid
'''
    headers: {
        'Content-Type': 'application/json'
    },
    body: {
        'username': {username},
        'password': {password}
    }
'''


class AuthUser(APIView):
    def post(self, request):
        reqData = dict(request.data)
        username = reqData['username']
        password = reqData['password']
        user = User.objects.filter(username=username, password=password)
        if len(user) != 1:
            return Response("Incorrect username/password", status.HTTP_401_UNAUTHORIZED)
        return Response(UserSerializer(user.first()).data, status.HTTP_200_OK)


# Registers a user via a POST request, returns an object if the user does not exist and the user model passed via the body is valid, or a 418 IM A TEAPOT if the user already exists, or a 500 INTERNAL_SERVER_ERROR if the model is invalid.
'''
    headers: {
        'Content-Type': 'application/json'
    },
    body: {
        'username':     {username},
        'password':     {password},
        'name':         {name},
        'email':        {email},
        'avatar_url':   {avatar_url},
        'chats':        [{chat_id}, {chat_id}]  //optional, preferred to be left blank upon initial account creation
        'id':           {id}                    //optional, preferred to be left blank upon initial account creation
    }
'''


class Register(APIView):
    def post(self, request):
        reqData = dict(request.data)
        username = reqData['username']
        user = User.objects.filter(username=username).first()
        if user is None:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Something went wrong. Please verify the object you're sending is a valid User object.", status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response("Username already exists", status.HTTP_418_IM_A_TEAPOT)

# Takes a GET request with no parameters, returns a list of all chats


class ListChats(APIView):
    def get(self, request, format=None):
        return Response(ChatSerializer(Chat.objects.all(), many=True).data)

# Takes a GET request with user ID in URL path, returns a list of all chats for a given user id, see urls.py for more documentation.


class ListChatsForUser(APIView):
    def get(self, request, format=None, UID=None):
        userid = self.kwargs['UID']
        return Response(ChatSerializer(Chat.objects.filter(users__in=[userid]), many=True).data)

# Takes a GET request with no parameters, returns a list of all messages


class ListMessages(APIView):
    def get(self, request, format=None):
        return Response(MessageSerializer(Message.objects.all(), many=True).data)

# Takes a GET request with chat ID in URL path, returns a list of all messages for a given chat id, see urls.py for more documentation.


class ListMessagesForChat(APIView):
    def get(self, request, format=None, Chat=None):
        chatno = self.kwargs['Chat']
        return Response(MessageSerializer(Message.objects.filter(chat_id=chatno), many=True).data)
    # def get(self, request, format=None):
    #     pass

# kind of unneccessary, leaving for legacy implementations


class UserManage(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# unncessary, leaving for legacy implementations


class ChatManage(APIView):
    # creating a new chat
    # deleting a chat
    # archiving a chat
    # creating a new message in a chat
    # deleting a message in a chat
    # Editing chats (could be a feature)
    def post(self, request):
        serializer: ChatSerializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            userList = dict(request.data)['users']
            serializer.save()
            for uid in userList:
                user: UserModel = User.objects.filter(id=uid).first()
                if user is None:
                    print("ERROR HERE")
                    return Response("One or more user ids in this chat do not have a corresponding user.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                user.chats.add(dict(serializer.data)['id'])
                user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("The data sent in the request body does not conform to model type Chat, or one or more user ids sent in the users list does not have a corresponding user.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        serializer = ChatSerializer(data=request.data)

# TODO SEND BACK DATA FOR POST AS THE SAME AS GET IN ANY OTHER GET ENDPOINTS

# unncessary, leaving for legacy implementations


class MessageManage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Adds a user to a given chat via  PUT request
# Returns a 200 OK if both the user id and chat id are valid, but the body of the response is simply a message stating that the user is already in the chat.
# Returns a 200 OK if both the user id and chat id are valid, and returns a serialized chat object if the user is not already in the chat
# Returns a 500 INTERNAL_SERVER_ERROR if the user or chat does not exist.
'''
    headers: {
        'Content-Type': 'application/json'
    },
    body: {
        'chat_id': {chat_id},
        'user_id': {user_id}
    }
'''


class AddUserToChat(APIView):
    def put(self, request):
        reqDict = dict(request.data)
        chatid = reqDict['chat_id']
        userid = reqDict['user_id']
        chat: ChatModel = Chat.objects.filter(id=chatid).first()
        user: UserModel = User.objects.filter(id=userid).first()
        if chat is not None and user is not None:
            if userid in [chat.id for chat in chat.users.all()]:
                return Response("User is already in chat " + str(chatid), status=status.HTTP_200_OK)
            chat.users.add(userid)
            user.chats.add(chatid)
            chat.save()
            user.save()
            return Response(ChatSerializer(chat).data)
        else:
            return Response("Invalid chat or user ID provided.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Removes a user from a given chat via a PUT request
# Returns a 200 OK if both the user id and chat id are valid, but the body of the response is simply a message stating that the user is not in the chat.
# Returns a 200 OK if both the user id and chat id are valid, and returns a serialized chat object if the user is in the chat
# Returns a 500 INTERNAL_SERVER_ERROR if the user or chat does not exist.
'''
    headers: {
        'Content-Type': 'application/json'
    },
    body: {
        'chat_id': {chat_id},
        'user_id': {user_id}
    }
'''


class RemoveUserFromChat(APIView):
    def put(self, request):
        reqDict = dict(request.data)
        chatid = reqDict['chat_id']
        userid = reqDict['user_id']
        chat: ChatModel = Chat.objects.filter(id=chatid).first()
        user: UserModel = User.objects.filter(id=userid).first()
        if chat is not None and user is not None:
            if userid not in [chat.id for chat in chat.users.all()]:
                return Response("User is not in chat " + str(chatid), status=status.HTTP_200_OK)
            chat.users.remove(userid)
            user.chats.remove(chatid)
            chat.save()
            user.save()
            return Response(ChatSerializer(chat).data)
        else:
            return Response("Invalid chat or user ID provided.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
{
    user_id: number;
    newUsername: string;
}
'''
class ChangeUsername(APIView):
    def post(self, request):
        reqDict = dict(request.data)
        uid = reqDict['user_id']
        username = reqDict['newUsername']
        user: UserModel = User.objects.filter(id=uid).first()
        currentUser: UserModel = User.objects.filter(username=username).first()
        if currentUser is not None:
            return Response(f'User {username} already exists.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if user is None:
            return Response(f'User {uid} does not exist in users table.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user.username = username
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
class ChangeName(APIView):
    def post(self, request):
        reqDict = dict(request.data)
        uid = reqDict['user_id']
        name = reqDict['newName']
        user: UserModel = User.objects.filter(id=uid).first()
        if user is None:
            return Response(f'User {uid} does not exist in users table.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user.name = name
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

class ChangePassword(APIView):
    def post(self, request):
        reqDict = dict(request.data)
        uid = reqDict['user_id']
        password = reqDict['newPassword']
        old_password = reqDict['oldPassword']
        user: UserModel = User.objects.filter(id=uid,password=old_password).first()
        if user is None:
            return Response(f'User {uid} does not exist in users table. Or password was incorrect', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user.password = password;
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


class DeleteUser(APIView):
    def get(self, request, UID):
        uid = self.kwargs['UID']
        user: UserModel = User.objects.filter(id=uid).first()
        if user is None:
            return Response(f'User {uid} does not exist in users table.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user.delete()
        return Response("User successfully deleted.", status=status.HTTP_200_OK)


class ListNotifications():
    pass
    # getting notifications (once user reads, delete)

    # class ListArchive(APIView):

    # @api_view(["GET"])
    # def index(request):

    # Create your views here.
    # class UserList(generics.ListAPIView):
    # queryset = User.objects.all()
