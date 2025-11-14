from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Astrologer, AstroChatSession, KundliMatch, KundliProfile

User = get_user_model()


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class AstrologerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astrologer
        fields = ['id', 'user', 'name', 'bio', 'experience_years', 'specialities', 'rating']


class KundliProfileSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)

    class Meta:
        model = KundliProfile
        fields = ['id', 'user', 'birth_date', 'birth_time', 'birth_place', 'horoscope_data', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']


class KundliMatchSerializer(serializers.ModelSerializer):
    profile = KundliProfileSerializer(read_only=True)
    matched_profile = KundliProfileSerializer(read_only=True)

    class Meta:
        model = KundliMatch
        fields = ['id', 'profile', 'matched_profile', 'compatibility_score', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']


class AstroChatSessionSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)
    astrologer = AstrologerSerializer(read_only=True)

    class Meta:
        model = AstroChatSession
        fields = [
            'id',
            'user',
            'astrologer',
            'scheduled_at',
            'started_at',
            'ended_at',
            'status',
            'notes',
        ]
        read_only_fields = ['id', 'started_at', 'ended_at', 'status']
