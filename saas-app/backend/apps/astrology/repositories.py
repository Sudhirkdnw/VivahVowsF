from django.db.models import QuerySet

from .models import Astrologer, AstroChatSession, KundliMatch, KundliProfile


def list_astrologers() -> QuerySet[Astrologer]:
    return Astrologer.objects.all()


def list_kundli_profiles() -> QuerySet[KundliProfile]:
    return KundliProfile.objects.select_related('user')


def list_astro_sessions_for_user(user_id: int) -> QuerySet[AstroChatSession]:
    return AstroChatSession.objects.filter(user_id=user_id).select_related('astrologer')


def list_kundli_matches(profile_id: int) -> QuerySet[KundliMatch]:
    return KundliMatch.objects.filter(profile_id=profile_id).select_related('profile', 'matched_profile')
