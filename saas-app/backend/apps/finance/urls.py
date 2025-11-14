from rest_framework import routers

from .views import EmiScheduleViewSet, KycDocumentViewSet, LoanApplicationViewSet

router = routers.DefaultRouter()
router.register(r'finance/loans', LoanApplicationViewSet, basename='finance-loans')
router.register(r'finance/kyc-documents', KycDocumentViewSet, basename='finance-kyc-documents')
router.register(r'finance/emi-schedule', EmiScheduleViewSet, basename='finance-emi-schedule')
