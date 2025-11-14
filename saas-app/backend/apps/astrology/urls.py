from rest_framework import routers

from .views import AstrologerViewSet, AstroChatSessionViewSet, KundliMatchViewSet, KundliProfileViewSet

router = routers.DefaultRouter()
router.register(r'astrology/astrologers', AstrologerViewSet, basename='astrologers')
router.register(r'astrology/kundli-profiles', KundliProfileViewSet, basename='kundli-profiles')
router.register(r'astrology/kundli-matches', KundliMatchViewSet, basename='kundli-matches')
router.register(r'astrology/chat-sessions', AstroChatSessionViewSet, basename='astro-chat-sessions')
