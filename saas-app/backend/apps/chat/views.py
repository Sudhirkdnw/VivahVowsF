from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from .models import ChatMessage, ChatThread
from .serializers import ChatMessageSerializer, ChatThreadSerializer
from .services import add_participant, create_thread, send_message

User = get_user_model()


class ChatThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ChatThreadSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ChatThread.objects.all()

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related('participants__user', 'messages__sender')
        if self.request.user.is_staff:
            return qs
        return qs.filter(participants__user=self.request.user).distinct()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name', '')
        participant_ids = request.data.get('participant_ids', [])
        thread = create_thread(name)
        add_participant(thread, request.user)
        for user_id in participant_ids:
            user = User.objects.get(id=user_id)
            add_participant(thread, user)
        serializer = self.get_serializer(thread)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ChatMessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ChatMessage.objects.select_related('thread', 'sender')

    def get_queryset(self):
        thread_id = self.request.query_params.get('thread_id')
        qs = super().get_queryset()
        if thread_id:
            qs = qs.filter(thread_id=thread_id)
        if not self.request.user.is_staff:
            qs = qs.filter(thread__participants__user=self.request.user)
        return qs

    def perform_create(self, serializer):
        thread = ChatThread.objects.get(id=self.request.data['thread'])
        message = send_message(thread, self.request.user, serializer.validated_data['content'])
        serializer.instance = message
