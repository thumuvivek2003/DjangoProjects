from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('room/<str:room_name>/', views.room_detail, name='room_detail'),
    path('create-room/', views.create_room, name='create_room'),
    path('register/', views.register, name='register'),
    path('api/room/<str:room_name>/messages/', views.get_room_messages, name='get_room_messages'),
]