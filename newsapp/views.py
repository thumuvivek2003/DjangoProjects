from django.shortcuts import render
from .models import News

def home(request):
    news = News.objects.order_by('-published_at')
    return render(request, 'newsapp/home.html', {'news': news})
