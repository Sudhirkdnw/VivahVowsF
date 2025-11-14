from rest_framework import routers

from .views import DatingProfileViewSet, LikeViewSet, MatchPreferenceViewSet, MatchViewSet, ProfilePhotoViewSet

router = routers.DefaultRouter()
router.register(r'dating/profiles', DatingProfileViewSet, basename='dating-profiles')
router.register(r'dating/photos', ProfilePhotoViewSet, basename='dating-photos')
router.register(r'dating/preferences', MatchPreferenceViewSet, basename='dating-preferences')
router.register(r'dating/likes', LikeViewSet, basename='dating-likes')
router.register(r'dating/matches', MatchViewSet, basename='dating-matches')
