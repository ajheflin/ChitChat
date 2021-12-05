import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.serializers import Serializer
from .serializers import MessageSerializer, UserSerializer, ChatSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = str(self.scope['url_route']['kwargs']['chat_id'])
        print(self.channel_name)
        await self.channel_layer.group_add(self.chat_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.chat_id, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        await self.channel_layer.group_send(self.chat_id, {
            'type': 'chat.message',
            'chat': self.chat_id,
            'content': text_data_json['content'],
            'sender': text_data_json['sender'],
        })

    async def chat_message(self, event):
        message = MessageSerializer(data=event)
        if message.is_valid():
            message.save()
        await self.send(text_data=json.dumps(message.data))
