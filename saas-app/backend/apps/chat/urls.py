from rest_framework import routers

from .views import ChatMessageViewSet, ChatThreadViewSet

router = routers.DefaultRouter()
router.register(r'chat/threads', ChatThreadViewSet, basename='chat-threads')
router.register(r'chat/messages', ChatMessageViewSet, basename='chat-messages')
