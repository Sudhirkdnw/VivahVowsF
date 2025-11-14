from rest_framework import serializers

from .models import EmiSchedule, KycDocument, LoanApplication


class KycDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KycDocument
        fields = ['id', 'application', 'document_type', 'document_url', 'verified']


class EmiScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmiSchedule
        fields = ['id', 'application', 'installment_number', 'due_date', 'amount', 'paid']


class LoanApplicationSerializer(serializers.ModelSerializer):
    kyc_documents = KycDocumentSerializer(many=True, read_only=True)
    emi_schedule = EmiScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = LoanApplication
        fields = [
            'id',
            'user',
            'amount',
            'tenure_months',
            'purpose',
            'status',
            'created_at',
            'kyc_documents',
            'emi_schedule',
        ]
        read_only_fields = ['id', 'status', 'created_at', 'user']
