from django.db import models

# Create your models here.

class ContactForm(models.Model):
    subject_type = models.CharField(max_length=100)
    service_location = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email_address = models.TextField(max_length=50)
    message_problems = models.TextField(max_length=1000)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.email_address

    class Meta:
        ordering = ['-accepted_date']
