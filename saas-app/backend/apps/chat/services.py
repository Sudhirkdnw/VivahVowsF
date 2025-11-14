from django.contrib.auth import get_user_model

from .models import ChatMessage, ChatThread, ChatThreadParticipant

User = get_user_model()


def create_thread(name: str | None = None) -> ChatThread:
    return ChatThread.objects.create(name=name or '')


def add_participant(thread: ChatThread, user: User) -> ChatThreadParticipant:
    participant, _ = ChatThreadParticipant.objects.get_or_create(thread=thread, user=user)
    return participant


def send_message(thread: ChatThread, sender: User, content: str) -> ChatMessage:
    add_participant(thread, sender)
    message = ChatMessage.objects.create(thread=thread, sender=sender, content=content)
    return message
