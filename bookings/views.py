from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
import datetime
import time
from .models import Booking


def booking_page(request):
    return render(request, 'bookings.html')
'''
def booking_confirmation_page(request):  # this is origin attempt
    return render(request, 'booking_confirmation.html')
'''

def get_booking(request):
    bookings = Booking.objects.all()
    # bookings = Booking.objects.filter(booking_user=request.user) use this to filter by user results only
    context = {
        'bookings': bookings
    }
    #return render(request, 'booking/user_profile.html', context)   page for profile
    return render(request, 'booking/booking_confirmation.html', context)

class SendBookingFormTemplateView(TemplateView):
    template_name = 'booking/booking_confirmation.html'   #'index.html'

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
            # booking_user = request.user    asign user to the form to call againts
        )
        
        print(f"logger user {request.user}")
        new_booking = Booking.objects.get(pk=booking_form.id)
        messages.add_message(
            request, messages.SUCCESS, f"Thank you ."
            f" For your booking for {first_name}, we will contact you shortly to confirm.")
        context = {
            'booking': new_booking
        }
        return render(request, 'booking/booking_confirmation.html', context)
        # return HttpResponseRedirect(request.path)

