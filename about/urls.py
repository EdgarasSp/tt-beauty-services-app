from . import views
from django.urls import path
from .views import (ManageTemplateView, SendContactFormTemplateView)

urlpatterns = [
    path('about/', views.about_page, name='about'),

    path('manage', ManageTemplateView.as_view(), name='manage'),
    path('contact/contact_form', SendContactFormTemplateView.as_view(), name='book_xray'),
]
