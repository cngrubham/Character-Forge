from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.user_login, name='login'),
  path('user/profile/<int:user_id>/', views.user_profile, name='user_profile'),
  path('profile/create/', views.UserCreate.as_view(), name='create_user'),
  path('profile/<int:pk>/update/', views.UserUpdate.as_view(), name='update_user'),
  path('profile/<int:pk>/delete/', views.UserDelete.as_view(), name='delete_user'),
  path('character/<int:pk>/', views.character_detail, name='detail'),
  path('character/create/', views.CharacterCreate.as_view(), name='create_character'),
  path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name='update_character'),
  path('character/<int:pk>/delete/', views.CharacterDelete.as_view(), name='delete_character'),
]
