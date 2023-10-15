from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character, User
from .forms import UserForm, CharacterForm

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def user_login(request):
    return render(request, 'user/login.html')

def user_profile(request):
    return render(request, 'user/profile.html')

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'main_app/user_form.html'

    def get_success_url(self):
        return 'user/profile/' 

class UserUpdate(UpdateView):
  model = User
  fields = '__all__'

class UserDelete(DeleteView):
  model = User
  success_url = '/'

def character_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  character_form = CharacterForm()
  return render(request, 'character/detail.html', {'character': character})

class CharacterCreate(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'main_app/character_form.html'

class CharacterDelete(DeleteView):
  model = Character
  success_url = 'user/profile'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'alignment', 'experience', 'level']