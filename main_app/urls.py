from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.user_login, name='login'),
  path('profile/', views.user_profile, name='profile'),
  path('profile/update/', views.UserUpdate.as_view(), name='update_user'),
  path('profile/delete/', views.UserDelete.as_view(), name='delete_user'),
  path('profile/create/', views.UserCreate.as_view(), name='create_user'),
  path('character/create/', views.CharacterCreate.as_view(), name='create_character'),
  path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name='update_character'),
  path('character/<int:pk>/delete/', views.CharacterDelete.as_view(), name='delete_character'),
  path('character/<int:pk>/', views.character_detail, name='detail'),
]
