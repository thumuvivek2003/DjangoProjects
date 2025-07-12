from django.shortcuts import render

def home_view(request):
    return render(request, 'portfolio/home.html')

def about_view(request):
    return render(request, 'portfolio/about.html')

def contact_view(request):
    return render(request, 'portfolio/contact.html')
