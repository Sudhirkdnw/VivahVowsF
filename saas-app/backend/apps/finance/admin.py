from django.contrib import admin

from .models import EmiSchedule, KycDocument, LoanApplication


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'tenure_months', 'status', 'created_at')
    list_filter = ('status',)


@admin.register(KycDocument)
class KycDocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'document_type', 'verified')
    list_filter = ('verified',)


@admin.register(EmiSchedule)
class EmiScheduleAdmin(admin.ModelAdmin):
    list_display = ('application', 'installment_number', 'due_date', 'amount', 'paid')
    list_filter = ('paid',)
