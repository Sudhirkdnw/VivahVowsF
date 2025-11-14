from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ChatMessage, ChatThread, ChatThreadParticipant

User = get_user_model()


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatThreadParticipantSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)

    class Meta:
        model = ChatThreadParticipant
        fields = ['id', 'thread', 'user', 'joined_at']
        read_only_fields = ['id', 'joined_at', 'user']


class ChatMessageSerializer(serializers.ModelSerializer):
    sender = UserSummarySerializer(read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'thread', 'sender', 'content', 'created_at']
        read_only_fields = ['id', 'thread', 'sender', 'created_at']


class ChatThreadSerializer(serializers.ModelSerializer):
    participants = ChatThreadParticipantSerializer(many=True, read_only=True)
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatThread
        fields = ['id', 'name', 'created_at', 'participants', 'messages']
        read_only_fields = ['id', 'created_at']
