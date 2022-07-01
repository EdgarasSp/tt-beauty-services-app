from django.shortcuts import render


def services_page(request):
    return render(request, 'services.html')
