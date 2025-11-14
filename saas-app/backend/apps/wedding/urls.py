from rest_framework import routers

from .views import (
    VendorBookingViewSet,
    VendorCategoryViewSet,
    VendorViewSet,
    WeddingBudgetItemViewSet,
    WeddingGuestViewSet,
    WeddingProjectViewSet,
    WeddingTaskViewSet,
)

router = routers.DefaultRouter()
router.register(r'wedding/projects', WeddingProjectViewSet, basename='wedding-projects')
router.register(r'wedding/guests', WeddingGuestViewSet, basename='wedding-guests')
router.register(r'wedding/tasks', WeddingTaskViewSet, basename='wedding-tasks')
router.register(r'wedding/budget-items', WeddingBudgetItemViewSet, basename='wedding-budget-items')
router.register(r'wedding/vendor-categories', VendorCategoryViewSet, basename='vendor-categories')
router.register(r'wedding/vendors', VendorViewSet, basename='vendors')
router.register(r'wedding/vendor-bookings', VendorBookingViewSet, basename='vendor-bookings')
