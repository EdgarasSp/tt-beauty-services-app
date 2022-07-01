
from django.urls import path
from . import views
from .views import (SendContactFormTemplateView)


urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('contact/contact_form', SendContactFormTemplateView.as_view(),
         name='contact_form'),
]
