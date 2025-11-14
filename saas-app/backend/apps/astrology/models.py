from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Astrologer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='astrologer_profile')
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    specialities = models.JSONField(default=list, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.name


class KundliProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kundli_profiles')
    birth_date = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=255)
    horoscope_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"KundliProfile({self.user})"


class KundliMatch(models.Model):
    profile = models.ForeignKey(KundliProfile, on_delete=models.CASCADE, related_name='matches')
    matched_profile = models.ForeignKey(KundliProfile, on_delete=models.CASCADE, related_name='matched_with')
    compatibility_score = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('profile', 'matched_profile')

    def __str__(self) -> str:
        return f"KundliMatch({self.profile_id} -> {self.matched_profile_id})"


class AstroChatSession(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='astro_chat_sessions')
    astrologer = models.ForeignKey(Astrologer, on_delete=models.CASCADE, related_name='chat_sessions')
    scheduled_at = models.DateTimeField()
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"AstroChatSession({self.user} with {self.astrologer})"
