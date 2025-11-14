from rest_framework import serializers

from .models import Payment, Subscription, SubscriptionPlan


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'description', 'price', 'duration_days', 'features', 'is_active']


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(source='plan', queryset=SubscriptionPlan.objects.all(), write_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'plan_id', 'start_date', 'end_date', 'is_active']
        read_only_fields = ['id', 'user']


class PaymentSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    subscription_id = serializers.PrimaryKeyRelatedField(source='subscription', queryset=Subscription.objects.all(), write_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'subscription', 'subscription_id', 'amount', 'paid_at', 'payment_method', 'transaction_id']
        read_only_fields = ['id', 'paid_at']
