from django.shortcuts import render



def about_page(request):  ## added
    return render(request, 'about.html')