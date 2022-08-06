from . import views
from django.urls import path
from .views import (SendBookingFormTemplateView)  #ViewBookingConfirmTemplateView

urlpatterns = [
    path('bookings/', views.booking_page, name='booking'),
    path('booking/booking_form', SendBookingFormTemplateView.as_view(),
         name='book_form'),
    
    path('booking/booking_confirmation', views.get_booking,  #'booking/booking_confirmation', ViewBookingConfirmTemplateView.as_view()
         name='get_booking')  #booking_confirmation_page
]
