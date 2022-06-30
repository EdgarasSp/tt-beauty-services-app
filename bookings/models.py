from django.db import models

# Create your models here.


STATUS = ((0, "Pending"), (1, "Completed"))
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    service_location = models.CharField(max_length=20)
    service = models.CharField(max_length=50)
    message_problems = models.TextField(max_length=1000)
    # received_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.email_address

    # class Meta:
    #     ordering = ['-received_date']

