from django.contrib import admin

from .models import DatingProfile, Match, MatchPreference, ProfilePhoto, Like


@admin.register(DatingProfile)
class DatingProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline', 'created_at')
    search_fields = ('user__username',)


@admin.register(ProfilePhoto)
class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ('profile', 'image_url', 'is_primary', 'uploaded_at')
    list_filter = ('is_primary',)


@admin.register(MatchPreference)
class MatchPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'age_min', 'age_max', 'preferred_gender')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('liker', 'liked', 'created_at', 'is_match')
    list_filter = ('is_match',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('user_one', 'user_two', 'created_at')
    search_fields = ('user_one__username', 'user_two__username')
