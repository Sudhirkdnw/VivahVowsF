from django.contrib import admin

from .models import ChatMessage, ChatThread, ChatThreadParticipant


class ChatThreadParticipantInline(admin.TabularInline):
    model = ChatThreadParticipant
    extra = 0


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 0


@admin.register(ChatThread)
class ChatThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    inlines = [ChatThreadParticipantInline, ChatMessageInline]


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('thread', 'sender', 'created_at')


@admin.register(ChatThreadParticipant)
class ChatThreadParticipantAdmin(admin.ModelAdmin):
    list_display = ('thread', 'user', 'joined_at')
