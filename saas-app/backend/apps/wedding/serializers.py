from rest_framework import serializers

from .models import (
    Vendor,
    VendorBooking,
    VendorCategory,
    WeddingBudgetItem,
    WeddingGuest,
    WeddingProject,
    WeddingTask,
)


class WeddingGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingGuest
        fields = ['id', 'project', 'name', 'email', 'phone_number', 'rsvp_status']


class WeddingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingTask
        fields = ['id', 'project', 'title', 'description', 'due_date', 'status']


class WeddingBudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingBudgetItem
        fields = ['id', 'project', 'category', 'estimated_cost', 'actual_cost', 'notes']


class VendorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorCategory
        fields = ['id', 'name', 'description']


class VendorSerializer(serializers.ModelSerializer):
    category = VendorCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=VendorCategory.objects.all(), write_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_email', 'contact_phone', 'pricing_details', 'category', 'category_id']


class VendorBookingSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(source='vendor', queryset=Vendor.objects.all(), write_only=True)

    class Meta:
        model = VendorBooking
        fields = ['id', 'project', 'vendor', 'vendor_id', 'booking_date', 'amount', 'status']


class WeddingProjectSerializer(serializers.ModelSerializer):
    guests = WeddingGuestSerializer(many=True, read_only=True)
    tasks = WeddingTaskSerializer(many=True, read_only=True)
    budget_items = WeddingBudgetItemSerializer(many=True, read_only=True)
    vendor_bookings = VendorBookingSerializer(many=True, read_only=True)

    class Meta:
        model = WeddingProject
        fields = [
            'id',
            'user',
            'name',
            'date',
            'location',
            'description',
            'created_at',
            'guests',
            'tasks',
            'budget_items',
            'vendor_bookings',
        ]
        read_only_fields = ['id', 'created_at', 'user']
