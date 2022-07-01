from django.contrib import admin
from .models import ContactForm

# Register your models here.


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject_type', 'first_name', 'last_name', 'email_address',
                    'received_date', 'message_problems', 'status')
    readonly_fields = ['received_date']
    list_filter = ('status', 'received_date')
    search_fields = ['subject_type', 'email_address', 'last_name']
    actions = ['mark_completed']

    def mark_completed(self, request, queryset):
        queryset.update(status=True)

# admin.site.register(ContactForm)
