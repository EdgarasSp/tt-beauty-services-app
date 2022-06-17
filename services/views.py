from django.shortcuts import render



def services_page(request):  ## added
    return render(request, 'services.html')