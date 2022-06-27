from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContactForm

# Register your models here.

@admin.register(ContactForm)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('subject_type', 'first_name', 'last_name', 'email_address', 'received_date', 'message_problems')
    list_filter = ('received_date',)
    search_fields = ['subject_type', 'email_address', 'last_name']

# admin.site.register(ContactForm)
