from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class WeddingProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wedding_projects')
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"WeddingProject({self.name})"


class WeddingGuest(models.Model):
    project = models.ForeignKey(WeddingProject, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    rsvp_status = models.CharField(max_length=20, default='pending')

    def __str__(self) -> str:
        return f"WeddingGuest({self.name})"


class WeddingTask(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    project = models.ForeignKey(WeddingProject, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self) -> str:
        return f"WeddingTask({self.title})"


class WeddingBudgetItem(models.Model):
    project = models.ForeignKey(WeddingProject, on_delete=models.CASCADE, related_name='budget_items')
    category = models.CharField(max_length=255)
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2)
    actual_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"WeddingBudgetItem({self.category})"


class VendorCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Vendor(models.Model):
    category = models.ForeignKey(VendorCategory, on_delete=models.CASCADE, related_name='vendors')
    name = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    pricing_details = models.JSONField(default=dict, blank=True)

    def __str__(self) -> str:
        return self.name


class VendorBooking(models.Model):
    project = models.ForeignKey(WeddingProject, on_delete=models.CASCADE, related_name='vendor_bookings')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        unique_together = ('project', 'vendor', 'booking_date')

    def __str__(self) -> str:
        return f"VendorBooking({self.project} - {self.vendor})"
