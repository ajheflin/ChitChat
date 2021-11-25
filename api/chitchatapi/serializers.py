from chitchatapi.models import User, Chat
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("__all__")


class UserSerializer(serializers.ModelSerializer):
    chats = ChatSerializer(many=True).data

    class Meta:
        model = User
        fields = ("__all__")
