import json

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer


class AsyncChatConsumer(AsyncJsonWebsocketConsumer):
    # groups = ["chat"]

    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            "chat",
            self.channel_name
        )

        await self.accept()

    async def receive_json(self, content, **kwargs):
        await self.channel_layer.group_send("chat",{
            "type": "chat.message",
            "message": content
        })

    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "message": event["message"],
            },
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "chat",
            self.channel_name
        )
