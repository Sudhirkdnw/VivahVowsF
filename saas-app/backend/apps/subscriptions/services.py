from datetime import date, timedelta

from django.contrib.auth import get_user_model

from .models import Payment, Subscription, SubscriptionPlan

User = get_user_model()


def create_subscription(user: User, plan: SubscriptionPlan, start: date | None = None) -> Subscription:
    start_date = start or date.today()
    end_date = start_date + timedelta(days=plan.duration_days)
    subscription = Subscription.objects.create(user=user, plan=plan, start_date=start_date, end_date=end_date)
    return subscription


def cancel_subscription(subscription: Subscription) -> Subscription:
    subscription.is_active = False
    subscription.save()
    return subscription


def record_payment(subscription: Subscription, amount: float, method: str, transaction_id: str) -> Payment:
    payment = Payment.objects.create(
        subscription=subscription,
        amount=amount,
        payment_method=method,
        transaction_id=transaction_id,
    )
    return payment
