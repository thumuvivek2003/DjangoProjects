from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contact/', include('contactForm.urls')),
    path('tasks/', include('taskmanager.urls')),
]
