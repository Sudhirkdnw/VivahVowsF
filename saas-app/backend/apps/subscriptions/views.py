from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Payment, Subscription, SubscriptionPlan
from .serializers import PaymentSerializer, SubscriptionPlanSerializer, SubscriptionSerializer
from .services import cancel_subscription, create_subscription, record_payment


class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['is_active']
    search_fields = ['name']


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.select_related('plan', 'user')
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        plan = serializer.validated_data['plan']
        subscription = create_subscription(self.request.user, plan)
        serializer.instance = subscription

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        subscription = self.get_object()
        cancel_subscription(subscription)
        return Response(self.get_serializer(subscription).data)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('subscription', 'subscription__plan')
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(subscription__user=self.request.user)
        return qs

    def perform_create(self, serializer):
        subscription = serializer.validated_data['subscription']
        payment = record_payment(
            subscription,
            serializer.validated_data['amount'],
            serializer.validated_data['payment_method'],
            serializer.validated_data['transaction_id'],
        )
        serializer.instance = payment
