from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model

from .models import EmiSchedule, KycDocument, LoanApplication

User = get_user_model()


def create_loan_application(user: User, data: dict) -> LoanApplication:
    application = LoanApplication.objects.create(user=user, **data)
    return application


def submit_loan_application(application: LoanApplication) -> LoanApplication:
    application.status = 'submitted'
    application.save()
    return application


def add_kyc_document(application: LoanApplication, data: dict) -> KycDocument:
    return KycDocument.objects.create(application=application, **data)


def create_emi_schedule(application: LoanApplication, schedule_data: list[dict]) -> list[EmiSchedule]:
    installments = []
    for item in schedule_data:
        due_date = item['due_date']
        if isinstance(due_date, str):
            due_date = date.fromisoformat(due_date)
        amount = item['amount']
        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))
        installment, _ = EmiSchedule.objects.update_or_create(
            application=application,
            installment_number=item['installment_number'],
            defaults={'due_date': due_date, 'amount': amount, 'paid': item.get('paid', False)},
        )
        installments.append(installment)
    return installments
