from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Astrologer, AstroChatSession, KundliMatch, KundliProfile

User = get_user_model()


def create_kundli_profile(user: User, data: dict) -> KundliProfile:
    profile = KundliProfile.objects.create(user=user, **data)
    return profile


def record_kundli_match(profile: KundliProfile, matched_profile: KundliProfile, score: float, notes: str = '') -> KundliMatch:
    match, _ = KundliMatch.objects.update_or_create(
        profile=profile,
        matched_profile=matched_profile,
        defaults={'compatibility_score': score, 'notes': notes},
    )
    return match


def schedule_chat_session(user: User, astrologer: Astrologer, scheduled_at) -> AstroChatSession:
    session = AstroChatSession.objects.create(user=user, astrologer=astrologer, scheduled_at=scheduled_at)
    return session


def start_session(session: AstroChatSession) -> AstroChatSession:
    session.status = 'active'
    session.started_at = timezone.now()
    session.save()
    return session


def end_session(session: AstroChatSession, notes: str = '') -> AstroChatSession:
    session.status = 'completed'
    session.ended_at = timezone.now()
    session.notes = notes or session.notes
    session.save()
    return session
