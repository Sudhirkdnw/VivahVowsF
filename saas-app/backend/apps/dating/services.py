from django.contrib.auth import get_user_model
from django.db import transaction

from .models import DatingProfile, Like, Match, MatchPreference, ProfilePhoto

User = get_user_model()


def get_or_create_dating_profile(user: User) -> DatingProfile:
    profile, _ = DatingProfile.objects.get_or_create(user=user)
    return profile


def update_dating_profile(user: User, data: dict) -> DatingProfile:
    profile = get_or_create_dating_profile(user)
    for attr, value in data.items():
        setattr(profile, attr, value)
    profile.save()
    return profile


def set_match_preference(user: User, data: dict) -> MatchPreference:
    preference, _ = MatchPreference.objects.get_or_create(user=user)
    for attr, value in data.items():
        setattr(preference, attr, value)
    preference.save()
    return preference


def add_photo(profile: DatingProfile, image_url: str, is_primary: bool = False) -> ProfilePhoto:
    if is_primary:
        profile.photos.update(is_primary=False)
    return ProfilePhoto.objects.create(profile=profile, image_url=image_url, is_primary=is_primary)


@transaction.atomic
def like_user(liker: User, liked: User) -> Like:
    like, created = Like.objects.get_or_create(liker=liker, liked=liked)
    if created:
        reverse_like = Like.objects.filter(liker=liked, liked=liker).first()
        if reverse_like:
            like.is_match = True
            like.save()
            reverse_like.is_match = True
            reverse_like.save()
            Match.objects.get_or_create(user_one=min(liker, liked, key=lambda u: u.id), user_two=max(liker, liked, key=lambda u: u.id))
    return like
