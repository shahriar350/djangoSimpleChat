from channels.consumer import AsyncConsumer

class AsyncChat(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect')
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self,event):
        print('websocket receive')

    async def websocket_disconnect(self,event):
        print('websocket disconnect')