from . import views
from django.urls import path


urlpatterns = [
    path('services/', views.services_page, name='services')
]
