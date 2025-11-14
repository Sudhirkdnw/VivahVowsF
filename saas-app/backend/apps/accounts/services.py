from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .repositories import get_user_by_id

User = get_user_model()


def create_user(username: str, email: str, password: str) -> User:
    user = User(username=username, email=email, password=make_password(password))
    user.save()
    UserProfile.objects.get_or_create(user=user)
    return user


def update_user_profile(user: User, profile_data: dict) -> UserProfile:
    profile, _ = UserProfile.objects.get_or_create(user=user)
    for attr, value in profile_data.items():
        setattr(profile, attr, value)
    profile.save()
    return profile


def retrieve_user(user_id: int) -> User:
    return get_user_by_id(user_id)
