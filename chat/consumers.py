import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message, RoomMember

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Update user online status
        await self.update_user_online_status(True)
        
        # Send user joined message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'user': self.user.username,
                'message': f'{self.user.username} joined the chat'
            }
        )

    async def disconnect(self, close_code):
        # Update user online status
        await self.update_user_online_status(False)
        
        # Send user left message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_left',
                'user': self.user.username,
                'message': f'{self.user.username} left the chat'
            }
        )
        
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Save message to database
        await self.save_message(message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'timestamp': self.get_timestamp()
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user': user,
            'timestamp': timestamp
        }))

    async def user_joined(self, event):
        user = event['user']
        message = event['message']
        
        # Send user joined message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'user_joined',
            'user': user,
            'message': message
        }))

    async def user_left(self, event):
        user = event['user']
        message = event['message']
        
        # Send user left message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'user_left',
            'user': user,
            'message': message
        }))

    @database_sync_to_async
    def save_message(self, message):
        room = Room.objects.get(name=self.room_name)
        Message.objects.create(
            room=room,
            user=self.user,
            content=message
        )

    @database_sync_to_async
    def update_user_online_status(self, is_online):
        room = Room.objects.get(name=self.room_name)
        room_member, created = RoomMember.objects.get_or_create(
            room=room,
            user=self.user,
            defaults={'is_online': is_online}
        )
        if not created:
            room_member.is_online = is_online
            room_member.save()

    def get_timestamp(self):
        from django.utils import timezone
        return timezone.now().strftime('%Y-%m-%d %H:%M:%S')