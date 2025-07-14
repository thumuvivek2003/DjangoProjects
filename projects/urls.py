from django.contrib import admin
from django.urls import path, include
from taskmanager.views import home_view
from django.conf import settings
from django.conf.urls.static import static

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
    path('gallery/', include('gallery.urls')),
    path('todoapi/', include('todoapi.urls')),
    path('weather/', include('weather.urls')),
    path('polls/', include('polls.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)