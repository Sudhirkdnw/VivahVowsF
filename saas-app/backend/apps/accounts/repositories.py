from django.contrib.auth import get_user_model
from django.db.models import QuerySet

User = get_user_model()


def get_users() -> QuerySet[User]:
    return User.objects.all()


def get_user_by_id(user_id: int) -> User:
    return User.objects.get(id=user_id)
