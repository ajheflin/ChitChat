from channels.generic.websocket import WebsocketConsumer
from django.http import response
from django.test import TestCase
from channels.testing import WebsocketCommunicator
from chitchatapi.consumer import ChatConsumer

# Create your tests here.


# Websocket Tests
class WebSocketTests(TestCase):
    async def test_connect(self):
        communicator = WebsocketCommunicator(
            ChatConsumer.as_asgi(), 'api/ws/chat/1/')
        connected, subprotocal = await communicator.connect()
        assert connected

        await communicator.send_json_to({'text': 'test_connect'})
        response = await communicator.receive_json_from()
        await communicator.disconnect()
