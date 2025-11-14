from rest_framework import routers

from .views import PaymentViewSet, SubscriptionPlanViewSet, SubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'subscriptions/plans', SubscriptionPlanViewSet, basename='subscription-plans')
router.register(r'subscriptions/subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register(r'subscriptions/payments', PaymentViewSet, basename='subscription-payments')
