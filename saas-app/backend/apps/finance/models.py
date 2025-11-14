from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class LoanApplication(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_applications')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tenure_months = models.PositiveIntegerField()
    purpose = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"LoanApplication({self.user} - {self.amount})"


class KycDocument(models.Model):
    application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name='kyc_documents')
    document_type = models.CharField(max_length=100)
    document_url = models.URLField()
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"KycDocument({self.document_type})"


class EmiSchedule(models.Model):
    application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name='emi_schedule')
    installment_number = models.PositiveIntegerField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.BooleanField(default=False)

    class Meta:
        unique_together = ('application', 'installment_number')

    def __str__(self) -> str:
        return f"EmiSchedule({self.installment_number})"
