from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('service', 'service_location', 'first_name', 'last_name', 'email_address')
    # readonly_fields = ['received_date']
    # list_filter = ('status', 'received_date')
    list_filter = ('service', 'service_location')
    search_fields = ['service', 'service_location', 'email_address', 'last_name']
    # actions = ['mark_completed']

    # def mark_completed(self, request, queryset):
    #     queryset.update(status=True)

