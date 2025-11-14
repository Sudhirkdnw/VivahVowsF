from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from .models import DatingProfile, Like, Match, MatchPreference

User = get_user_model()


def list_profiles() -> QuerySet[DatingProfile]:
    return DatingProfile.objects.select_related('user').prefetch_related('photos')


def list_matches_for_user(user: User) -> QuerySet[Match]:
    return Match.objects.filter(user_one=user) | Match.objects.filter(user_two=user)


def list_likes_for_user(user: User) -> QuerySet[Like]:
    return Like.objects.filter(liker=user)


def get_match_preference(user: User) -> MatchPreference:
    return MatchPreference.objects.get(user=user)
