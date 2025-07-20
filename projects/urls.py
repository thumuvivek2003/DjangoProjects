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
    path('shop/', include('shop2.urls')),
    path('news/', include('newsapp.urls')),
    path('news_aggregator/', include('news_aggregator.urls')),
    path('chat/', include('chat.urls')),
    path('jobs/', include('jobboard.urls')),
    path('resume/', include('resume_builder.urls')),
    path('social/', include('social_network2.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)