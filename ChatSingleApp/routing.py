from django.urls import path

from chat_app import consumers

websocket_urlpatters = [
    path('ws/chat/',consumers.AsyncChatConsumer.as_asgi())
]
