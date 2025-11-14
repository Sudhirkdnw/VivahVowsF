from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import EmiSchedule, KycDocument, LoanApplication
from .serializers import EmiScheduleSerializer, KycDocumentSerializer, LoanApplicationSerializer
from .services import add_kyc_document, create_emi_schedule, create_loan_application, submit_loan_application


class LoanApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = LoanApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = LoanApplication.objects.select_related('user')
    filterset_fields = ['status']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        application = create_loan_application(self.request.user, serializer.validated_data)
        serializer.instance = application

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        application = self.get_object()
        submit_loan_application(application)
        return Response(self.get_serializer(application).data)


class KycDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = KycDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = KycDocument.objects.select_related('application', 'application__user')

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(application__user=self.request.user)
        return qs

    def perform_create(self, serializer):
        application = serializer.validated_data.pop('application')
        document = add_kyc_document(application, serializer.validated_data)
        serializer.instance = document


class EmiScheduleViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = EmiScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = EmiSchedule.objects.select_related('application', 'application__user')

    def get_queryset(self):
        qs = super().get_queryset()
        application_id = self.request.query_params.get('application_id')
        if application_id:
            qs = qs.filter(application_id=application_id)
        if not self.request.user.is_staff:
            qs = qs.filter(application__user=self.request.user)
        return qs

    @action(detail=False, methods=['post'])
    def bulk(self, request):
        application = LoanApplication.objects.get(id=request.data['application_id'])
        schedule = create_emi_schedule(application, request.data.get('schedule', []))
        serializer = self.get_serializer(schedule, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
