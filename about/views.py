from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib import messages
import datetime
import time
from .models import ContactForm



def about_page(request):  ## home
    return render(request, 'about.html')


# class ManageTemplateView(TemplateView):
#     template_name = 'contact/contact_form.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     contactforms = ContactForm.objects.all()

    #     context.update({
    #         "contactforms":contactforms,
    #     })
    #     return context

    # def post(self, request):
    #     if request.POST.get("form_type") == 'contactus':
    #         email_address = request.POST.get("email_address")
    #         contactform = ContactForm.objects.get(email_address=email_address)
    #         # contactform.accepted = True
    #         contactform.received_date = datetime.datetime.now()
    #         contactform.save()
    #         console.log("top")
    #         return HttpResponseRedirect(request.path)



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

        messages.add_message(request, messages.SUCCESS, f"Thank you {first_name} {last_name}. For your message.")
        return HttpResponseRedirect(request.path)

