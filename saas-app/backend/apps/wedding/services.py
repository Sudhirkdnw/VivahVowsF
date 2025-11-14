from django.contrib.auth import get_user_model

from .models import (
    Vendor,
    VendorBooking,
    VendorCategory,
    WeddingBudgetItem,
    WeddingGuest,
    WeddingProject,
    WeddingTask,
)

User = get_user_model()


def create_wedding_project(user: User, data: dict) -> WeddingProject:
    project = WeddingProject.objects.create(user=user, **data)
    return project


def add_guest(project: WeddingProject, data: dict) -> WeddingGuest:
    return WeddingGuest.objects.create(project=project, **data)


def add_task(project: WeddingProject, data: dict) -> WeddingTask:
    return WeddingTask.objects.create(project=project, **data)


def add_budget_item(project: WeddingProject, data: dict) -> WeddingBudgetItem:
    return WeddingBudgetItem.objects.create(project=project, **data)


def book_vendor(project: WeddingProject, vendor: Vendor, data: dict) -> VendorBooking:
    return VendorBooking.objects.create(project=project, vendor=vendor, **data)


def create_vendor_category(data: dict) -> VendorCategory:
    return VendorCategory.objects.create(**data)


def create_vendor(data: dict) -> Vendor:
    return Vendor.objects.create(**data)
