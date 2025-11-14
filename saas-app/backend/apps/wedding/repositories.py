from django.db.models import Prefetch, QuerySet

from .models import (
    Vendor,
    VendorBooking,
    VendorCategory,
    WeddingBudgetItem,
    WeddingGuest,
    WeddingProject,
    WeddingTask,
)


def list_projects_for_user(user_id: int) -> QuerySet[WeddingProject]:
    return (
        WeddingProject.objects.filter(user_id=user_id)
        .prefetch_related(
            'guests',
            'tasks',
            'budget_items',
            Prefetch('vendor_bookings', queryset=VendorBooking.objects.select_related('vendor')),
        )
    )


def list_vendor_categories() -> QuerySet[VendorCategory]:
    return VendorCategory.objects.prefetch_related('vendors')


def list_vendors() -> QuerySet[Vendor]:
    return Vendor.objects.select_related('category')
