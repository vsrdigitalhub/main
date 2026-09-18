from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ContactMessage, CustomUser, Service, ServiceInquiry


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    All customer accounts, backed by the MySQL `core_customuser` table.
    Lets VSR staff view/search/manage every registered customer.
    """
    fieldsets = UserAdmin.fieldsets + (
        ("VSR Profile", {
            "fields": ("phone_number", "company_name", "address", "is_customer")
        }),
    )
    list_display = ("username", "email", "phone_number", "company_name", "is_staff", "date_joined")
    search_fields = ("username", "email", "phone_number", "company_name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order")
    ordering = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_resolved")
    list_filter = ("is_resolved", "created_at")
    search_fields = ("name", "email", "subject", "message")


@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = ("user", "service", "status", "created_at")
    list_filter = ("status", "service")
    search_fields = ("user__username", "details")
