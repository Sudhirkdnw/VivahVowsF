from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import DatingProfile, Like, Match, MatchPreference, ProfilePhoto

User = get_user_model()


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePhoto
        fields = ['id', 'image_url', 'is_primary', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']


class DatingProfileSerializer(serializers.ModelSerializer):
    photos = ProfilePhotoSerializer(many=True, read_only=True)
    user = UserSummarySerializer(read_only=True)

    class Meta:
        model = DatingProfile
        fields = ['id', 'user', 'headline', 'about', 'interests', 'preferences', 'photos', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']


class MatchPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPreference
        fields = ['id', 'age_min', 'age_max', 'preferred_gender', 'location', 'interests']
        read_only_fields = ['id']


class LikeSerializer(serializers.ModelSerializer):
    liker = UserSummarySerializer(read_only=True)
    liked = UserSummarySerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'liker', 'liked', 'created_at', 'is_match']
        read_only_fields = ['id', 'created_at', 'is_match']


class MatchSerializer(serializers.ModelSerializer):
    user_one = UserSummarySerializer(read_only=True)
    user_two = UserSummarySerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['id', 'user_one', 'user_two', 'created_at']
        read_only_fields = ['id', 'created_at']
