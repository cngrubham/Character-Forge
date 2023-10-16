from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('user/user_index/', views.user_index, name='user_index'),
    path('user/user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/create/', views.UserCreate.as_view(), name='create_user'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='update_user'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='delete_user'),
    
    path('character/<int:pk>/', views.character_detail, name='detail'),
    path('character/create/', views.character_create, name='create_character'),
    path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name='update_character'),
    path('character/<int:pk>/delete/', views.CharacterDelete.as_view(), name='delete_character'),
    path('character_demo/', views.character_demo, name='character_demo'),
    path('alignment/<str:alignment_name>/', views.char_profile_demo, name='char_profile_demo'),
    path('races_index/', views.races_index, name='races_index'),
    path('races_index/<str:race_name>/', views.race, name='race')
]
