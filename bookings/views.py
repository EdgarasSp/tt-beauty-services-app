from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
import datetime
import time
from .models import Booking

def booking_page(request):  ## home
    return render(request, 'bookings.html')

class SendBookingFormTemplateView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        service = request.POST.get('service')
        service_location = request.POST.get('service_location')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')
        message_problems = request.POST.get('message_problems')

        booking_form = Booking.objects.create(
            service=service,
            service_location=service_location,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email_address=email_address,
            message_problems=message_problems,
        )
        
        booking_form.save()

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name}. For your booking, we will contact you shortly to confirm.")
        return HttpResponseRedirect(request.path)

