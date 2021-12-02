from chitchatapi.models import Message, User, Chat
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("__all__")

    # def create(self, validated_data):
    #     print(validated_data)
    #     chat = Chat.objects.get_or_create(**validated_data)
    #     return chat


class UserSerializer(serializers.ModelSerializer):
    chats = ChatSerializer(many=True).data

    class Meta:
        model = User
        fields = ("__all__")


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer().data

    class Meta:
        model = Message
        fields = ("__all__")
