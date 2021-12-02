from django.conf.urls import url
from django.urls import re_path
from django.core.asgi import get_asgi_application

from . import consumer

websocket_urlpatterns = [
    re_path(r'^api/ws/chat/(?P<chat_id>.?)/$',
            consumer.ChatConsumer.as_asgi()),
]
