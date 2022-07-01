from . import views
from django.urls import path
from .views import (SendBookingFormTemplateView)

urlpatterns = [
    path('bookings/', views.booking_page, name='booking'),
    path('booking/booking_form', SendBookingFormTemplateView.as_view(),
         name='book_form')
]
