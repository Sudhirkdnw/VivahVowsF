from django.contrib import admin

from .models import Astrologer, AstroChatSession, KundliMatch, KundliProfile


@admin.register(Astrologer)
class AstrologerAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience_years', 'rating')
    search_fields = ('name',)


@admin.register(KundliProfile)
class KundliProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'birth_place', 'created_at')
    search_fields = ('user__username', 'birth_place')


@admin.register(KundliMatch)
class KundliMatchAdmin(admin.ModelAdmin):
    list_display = ('profile', 'matched_profile', 'compatibility_score', 'created_at')


@admin.register(AstroChatSession)
class AstroChatSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'astrologer', 'scheduled_at', 'status')
    list_filter = ('status',)
