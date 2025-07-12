from django.contrib import admin
from django.urls import path, include
from taskmanager.views import home_view

urlpatterns = [
    path('', home_view, name='home2'),
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contact/', include('contactForm.urls')),
    path('tasks/', include('taskmanager.urls')),
    path('accounts/', include('accounts.urls')),
    path('notes/', include('notes.urls')),
]
