from django.contrib import admin

from .models import (
    Vendor,
    VendorBooking,
    VendorCategory,
    WeddingBudgetItem,
    WeddingGuest,
    WeddingProject,
    WeddingTask,
)


@admin.register(WeddingProject)
class WeddingProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date', 'location')
    search_fields = ('name', 'user__username')


@admin.register(WeddingGuest)
class WeddingGuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'rsvp_status')
    list_filter = ('rsvp_status',)


@admin.register(WeddingTask)
class WeddingTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date')
    list_filter = ('status',)


@admin.register(WeddingBudgetItem)
class WeddingBudgetItemAdmin(admin.ModelAdmin):
    list_display = ('project', 'category', 'estimated_cost', 'actual_cost')


@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'contact_email', 'contact_phone')


@admin.register(VendorBooking)
class VendorBookingAdmin(admin.ModelAdmin):
    list_display = ('project', 'vendor', 'booking_date', 'amount', 'status')
    list_filter = ('status',)
