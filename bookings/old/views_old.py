from django.shortcuts import render



def bookings_page(request):  ## added
    return render(request, 'bookings.html')