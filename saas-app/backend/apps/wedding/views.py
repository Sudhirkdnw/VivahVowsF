from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import (
    Vendor,
    VendorBooking,
    VendorCategory,
    WeddingBudgetItem,
    WeddingGuest,
    WeddingProject,
    WeddingTask,
)
from .serializers import (
    VendorBookingSerializer,
    VendorCategorySerializer,
    VendorSerializer,
    WeddingBudgetItemSerializer,
    WeddingGuestSerializer,
    WeddingProjectSerializer,
    WeddingTaskSerializer,
)


class WeddingProjectViewSet(viewsets.ModelViewSet):
    serializer_class = WeddingProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WeddingProject.objects.all()
    filterset_fields = ['date']
    search_fields = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WeddingGuestViewSet(viewsets.ModelViewSet):
    serializer_class = WeddingGuestSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WeddingGuest.objects.select_related('project')
    filterset_fields = ['project__id', 'rsvp_status']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(project__user=self.request.user)
        return qs


class WeddingTaskViewSet(viewsets.ModelViewSet):
    serializer_class = WeddingTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WeddingTask.objects.select_related('project')
    filterset_fields = ['project__id', 'status']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(project__user=self.request.user)
        return qs


class WeddingBudgetItemViewSet(viewsets.ModelViewSet):
    serializer_class = WeddingBudgetItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WeddingBudgetItem.objects.select_related('project')
    filterset_fields = ['project__id']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(project__user=self.request.user)
        return qs


class VendorCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = VendorCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = VendorCategory.objects.all()


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Vendor.objects.select_related('category')


class VendorBookingViewSet(viewsets.ModelViewSet):
    serializer_class = VendorBookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = VendorBooking.objects.select_related('project', 'vendor')
    filterset_fields = ['project__id', 'status']

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(project__user=self.request.user)
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
