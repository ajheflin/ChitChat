from channels.generic.websocket import WebsocketConsumer
from django.http import response
from django.test import TestCase
from channels.testing import WebsocketCommunicator
from chitchatapi.consumer import ChatConsumer
from channels.routing import URLRouter
from django.conf.urls import url

# Create your tests here.


# Websocket Tests
class WebSocketTests(TestCase):
    async def test_connect(self):
        # communicator = WebsocketCommunicator(URLRouter([
        #     '/api/ws/chat/1/', ChatConsumer.as_asgi()),
        # ]))
        connected, subprotocal = await communicator.connect()
        assert connected

        # await communicator.send_to({'text': 'test_connect'})
        response = await communicator.receive_from()
        await communicator.disconnect()
