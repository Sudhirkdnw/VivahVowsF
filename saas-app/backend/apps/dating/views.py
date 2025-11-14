from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import DatingProfile, Like, Match, MatchPreference, ProfilePhoto
from .serializers import (
    DatingProfileSerializer,
    LikeSerializer,
    MatchPreferenceSerializer,
    MatchSerializer,
    ProfilePhotoSerializer,
)
from .services import add_photo, get_or_create_dating_profile, like_user, set_match_preference, update_dating_profile

User = get_user_model()


class DatingProfileViewSet(viewsets.ModelViewSet):
    serializer_class = DatingProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = DatingProfile.objects.select_related('user').prefetch_related('photos')
    filterset_fields = ['user__id']

    def get_queryset(self):
        qs = super().get_queryset()
        user_only = self.request.query_params.get('mine')
        if user_only == 'true':
            return qs.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'])
    def update_profile(self, request):
        profile = update_dating_profile(request.user, request.data)
        return Response(self.get_serializer(profile).data)


class ProfilePhotoViewSet(viewsets.ModelViewSet):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProfilePhoto.objects.select_related('profile__user')

    def perform_create(self, serializer):
        profile = get_or_create_dating_profile(self.request.user)
        photo = add_photo(profile, serializer.validated_data['image_url'], serializer.validated_data.get('is_primary', False))
        serializer.instance = photo

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(profile__user=self.request.user)


class MatchPreferenceViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = MatchPreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = MatchPreference.objects.select_related('user')

    def get_object(self):
        obj, _ = MatchPreference.objects.get_or_create(user=self.request.user)
        return obj

    def update(self, request, *args, **kwargs):
        preference = set_match_preference(request.user, request.data)
        serializer = self.get_serializer(preference)
        return Response(serializer.data)


class LikeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.select_related('liker', 'liked')

    def get_queryset(self):
        return self.queryset.filter(liker=self.request.user)

    def create(self, request, *args, **kwargs):
        liked_id = request.data.get('liked_id')
        liked_user = User.objects.get(id=liked_id)
        like = like_user(request.user, liked_user)
        serializer = self.get_serializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MatchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Match.objects.select_related('user_one', 'user_two')

    def get_queryset(self):
        return self.queryset.filter(user_one=self.request.user) | self.queryset.filter(user_two=self.request.user)
