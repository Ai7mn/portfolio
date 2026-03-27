from django.contrib import admin
from .models import CV, ContactUs


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "active", "timestamp")
    list_filter = ("active",)
    search_fields = ("file",)
    ordering = ("-timestamp",)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("sender_name", "sender_email", "timeStamp")
    list_filter = ("timeStamp",)
    search_fields = ("sender_name", "sender_email", "message")
    readonly_fields = ("timeStamp",)
    ordering = ("-timeStamp",)
