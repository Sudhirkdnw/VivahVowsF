import json
from typing import Any

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from .models import ChatMessage, ChatThread
from .services import add_participant, send_message

User = get_user_model()

authenticator = JWTAuthentication()


@database_sync_to_async
def get_thread(thread_id: int) -> ChatThread:
    return ChatThread.objects.get(id=thread_id)


@database_sync_to_async
def add_participant_sync(thread: ChatThread, user: User):
    return add_participant(thread, user)


@database_sync_to_async
def send_message_sync(thread: ChatThread, user: User, content: str) -> ChatMessage:
    return send_message(thread, user, content)


@database_sync_to_async
def serialize_message(message: ChatMessage) -> dict[str, Any]:
    return {
        'id': message.id,
        'thread': message.thread_id,
        'sender': {'id': message.sender_id, 'username': message.sender.username},
        'content': message.content,
        'created_at': message.created_at.isoformat(),
    }


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.thread_id = int(self.scope['url_route']['kwargs']['thread_id'])
        self.user = await self.authenticate_user()
        if not self.user:
            await self.close(code=4001)
            return
        try:
            self.thread = await get_thread(self.thread_id)
        except ObjectDoesNotExist:
            await self.close(code=4004)
            return
        await add_participant_sync(self.thread, self.user)
        self.group_name = f'chat_{self.thread_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'group_name'):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            content = data.get('content')
            if not content:
                return
            message = await send_message_sync(self.thread, self.user, content)
            payload = await serialize_message(message)
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': payload,
                },
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event['message']))

    async def authenticate_user(self):
        headers = dict(self.scope.get('headers') or [])
        token = None
        auth_header = headers.get(b'authorization')
        if auth_header:
            parts = auth_header.decode().split(' ')
            if len(parts) == 2:
                token = parts[1]
        else:
            query_string = self.scope.get('query_string', b'').decode()
            for part in query_string.split('&'):
                if part.startswith('token='):
                    token = part.split('=', 1)[1]
                    break
        if not token:
            return None
        try:
            validated = authenticator.get_validated_token(token)
            user = await database_sync_to_async(authenticator.get_user)(validated)
            return user
        except InvalidToken:
            return None
