from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
import datetime
import time
from .models import ContactForm



def about_page(request):  ## added
    return render(request, 'about.html')

class ManageTemplateView(TemplateView):
    template_name = '#'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contactforms = ContactForm.objects.all()

        context.update({
            "contactforms": contactforms,
        })
        return context

    def post(self, request):
        if request.POST.get("form_type") == 'contactusform':
            email_address = request.POST.get("email_address")
            contactform = ContactForm.objects.get(email_address=email_address)
            contactform.accepted = True
            contactform.accepted_date = datetime.datetime.now()
            contactform.save()
        return HttpResponseRedirect(request.path)



class SendContactFormTemplateView(TemplateView):
    template_name = 'contact/contact_form.html'

    def post(self, request):
        subject_type = request.POST.get('subject_type')
        service_location = request.POST.get('service_location')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        email_address = request.POST.get('email_address')
        message_problems = request.POST.get('message_problems')



        # if first_name and last_name and exam_location and date_of_exam and time_of_exam:
        #     try:
        #         send_mail(
        #             subject=f"Your radiology appointment",
        #             message=f"{first_name} {last_name},\n\nYou booked an x-ray appointment via ELHT Radiology Booking service.\n\nAppointment date: {date_of_exam}\nAppointment time: {time_of_exam}\nLocation: {exam_location}. \n\nIf you are unable to make your appointment please let us know as soon as possible quoting your reference number: {ref_number}.",
        #             from_email=settings.EMAIL_HOST_USER,
        #             recipient_list=[email_address])
        #         send_mail(
        #             subject=f"New booking via ELHT RBS",
        #             message=f"{first_name} {last_name} just made a booking for x-ray via ELHT RBS. Log in to admin page to confirm this booking.",
        #             from_email=settings.EMAIL_HOST_USER,
        #             recipient_list=[settings.EMAIL_HOST_USER])
        #     except BadHeaderError:
        #         return HttpResponse('Invalid header found.')
        # else:
        #     return HttpResponse('Make sure all fields are entered and valid.')

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

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. For your message.")
        return HttpResponseRedirect(request.path)

