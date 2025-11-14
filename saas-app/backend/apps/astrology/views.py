from datetime import datetime

from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Astrologer, AstroChatSession, KundliMatch, KundliProfile
from .serializers import (
    AstrologerSerializer,
    AstroChatSessionSerializer,
    KundliMatchSerializer,
    KundliProfileSerializer,
)
from .services import end_session, schedule_chat_session, start_session


class AstrologerViewSet(viewsets.ModelViewSet):
    queryset = Astrologer.objects.all()
    serializer_class = AstrologerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['experience_years']
    search_fields = ['name']


class KundliProfileViewSet(viewsets.ModelViewSet):
    queryset = KundliProfile.objects.select_related('user')
    serializer_class = KundliProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs


class KundliMatchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = KundliMatchSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = KundliMatch.objects.select_related('profile', 'matched_profile')

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        qs = super().get_queryset()
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs


class AstroChatSessionViewSet(viewsets.ModelViewSet):
    serializer_class = AstroChatSessionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = AstroChatSession.objects.select_related('user', 'astrologer')
    filterset_fields = ['status']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    def create(self, request, *args, **kwargs):
        astrologer_id = request.data.get('astrologer_id')
        scheduled_at = request.data.get('scheduled_at')
        astrologer = Astrologer.objects.get(id=astrologer_id)
        if isinstance(scheduled_at, str):
            scheduled_at_value = datetime.fromisoformat(scheduled_at)
        else:
            scheduled_at_value = scheduled_at
        session = schedule_chat_session(request.user, astrologer, scheduled_at_value)
        serializer = self.get_serializer(session)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        session = self.get_object()
        start_session(session)
        return Response(self.get_serializer(session).data)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        session = self.get_object()
        notes = request.data.get('notes', '')
        end_session(session, notes)
        return Response(self.get_serializer(session).data)
