from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
import datetime
import time
from .models import ContactForm


def about_page(request):
    return render(request, 'about.html')


class SendContactFormTemplateView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        subject_type = request.POST.get('subject_type')
        service_location = request.POST.get('service_location')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')
        message_problems = request.POST.get('message_problems')

        contact_form = ContactForm.objects.create(
            subject_type=subject_type,
            service_location=service_location,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email_address=email_address,
            message_problems=message_problems,
        )

        contact_form.save()

        messages.add_message(request, messages.SUCCESS ,
                            f"Thank you {first_name} . For your message we will reply within 24h.")
        return HttpResponseRedirect(request.path)
