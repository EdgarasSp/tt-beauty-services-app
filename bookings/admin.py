from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('service', 'service_location', 'first_name', 'last_name', 'email_address', 'message_problems', 'status')
    readonly_fields = ['received_date']
    list_filter = ('status', 'service', 'service_location', 'received_date')
    search_fields = ['service', 'service_location', 'email_address', 'last_name']
    actions = ['mark_responded']

    def mark_responded(self, request, queryset):
        queryset.update(status=True)

