from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class DatingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dating_profile')
    headline = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    interests = models.JSONField(default=list, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"DatingProfile({self.user})"


class ProfilePhoto(models.Model):
    profile = models.ForeignKey(DatingProfile, on_delete=models.CASCADE, related_name='photos')
    image_url = models.URLField()
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_primary', '-uploaded_at']

    def __str__(self) -> str:
        return f"Photo({self.profile.user})"


class MatchPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='match_preference')
    age_min = models.PositiveIntegerField(default=18)
    age_max = models.PositiveIntegerField(default=60)
    preferred_gender = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=255, blank=True)
    interests = models.JSONField(default=list, blank=True)

    def __str__(self) -> str:
        return f"MatchPreference({self.user})"


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_given')
    liked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_received')
    created_at = models.DateTimeField(auto_now_add=True)
    is_match = models.BooleanField(default=False)

    class Meta:
        unique_together = ('liker', 'liked')

    def __str__(self) -> str:
        return f"Like({self.liker} -> {self.liked})"


class Match(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_one')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_two')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_one', 'user_two')

    def __str__(self) -> str:
        return f"Match({self.user_one} & {self.user_two})"
