from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.resume_create, name='resume_create'),
    path('<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('<int:pk>/preview/', views.resume_preview, name='resume_preview'),
    path('<int:pk>/download/', views.resume_download_pdf, name='resume_download_pdf'),
    path('<int:pk>/delete/', views.resume_delete, name='resume_delete'),
]