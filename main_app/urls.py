from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('character_demo/', views.character_demo, name='character_demo'),
    path('alignment/<str:alignment_name>/', views.char_profile_demo, name='char_profile_demo'),
    path('races_index/', views.races_index, name='races_index'),
    path('races_index/<str:race_name>/', views.race, name='race')


]