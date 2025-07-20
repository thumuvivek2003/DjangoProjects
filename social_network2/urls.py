from django.urls import path
from . import views

app_name = 'social_network'

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    
    # Main pages
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.user_search, name='search'),
    
    # AJAX endpoints
    path('follow/', views.follow_user, name='follow_user'),
    path('like/', views.like_content, name='like_content'),
    path('comment/', views.add_comment, name='add_comment'),
]