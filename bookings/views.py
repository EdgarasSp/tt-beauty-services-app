from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
import datetime
import time
from .models import Booking


def booking_page(request):
    return render(request, 'bookings.html')

'''
def booking_confirmation_page(request):
    return render(request, 'booking_confirmation.html')
'''


class SendBookingFormTemplateView(TemplateView):
    template_name = 'index.html'   #'booking/booking_confirmation.html'

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

        messages.add_message(
            request, messages.SUCCESS, f"Thank you {first_name}."
            f" For your booking, we will contact you shortly to confirm.")
        return HttpResponseRedirect(request.path)

'''
class ViewBookingConfirmTemplateView(TemplateView):
    template_name = 'booking/booking_confirmation.html'

    def booking_confirm(self, request):
        if request.method == "GET":
            service = request.GET.get('service')
            service_location = request.GET.get('service_location')
            first_name = request.GET.get('first_name')
            last_name = request.GET.get('last_name')
            contact_number = request.GET.get('contact_number')
            email_address = request.GET.get('email_address')
            message_problems = request.GET.get('message_problems')

            messages.add_message(
            request, messages.SUCCESS, f"if {first_name}."
            f" Works.")
        
        
            return render(
                request,
                "booking/booking_confirmation.html",
                {
                    "first_name": first_name,
                })
              

        return HttpResponseRedirect(request.path)
        '''