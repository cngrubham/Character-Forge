from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character, User
from .forms import UserForm, CharacterForm
from django.urls import reverse
import requests


# Define the home view
def home(request):
  return render(request, 'home.html')

def user_login(request):
    return render(request, 'user/login.html')

def user_profile(request, user_id):
    characters = Character.objects.all()
    # will probably need to change.all to display only specific user characters
    return render(request, 'user/profile.html', {'characters': characters})

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'main_app/user_form.html'

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse('user_profile', args=[user.id]))

class UserUpdate(UpdateView):
  model = User
  fields = '__all__'

class UserDelete(DeleteView):
  model = User
  success_url = '/'

def character_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  return render(request, 'character/detail.html', {'character': character})

class CharacterCreate(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'main_app/character_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user_profile')

class CharacterDelete(DeleteView):
  model = Character
  success_url = 'user/profile'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'alignment', 'experience', 'level']

def character_demo(request):
  response=requests.get('https://www.dnd5eapi.co/api/alignments').json()
  print(response)
  return render(request, 'characters/character_demo.html', {'response':response})

def char_profile_demo(request, alignment_name):
  alignment_name = alignment_name.lower().replace(" ", "-")
  response=requests.get(f'https://www.dnd5eapi.co/api/alignments/{alignment_name}').json()
  print(response)
  name = response.get('name', '')
  desc = response.get('desc', '')

  return render(request, 'characters/char_profile_demo.html', {'name': name, 'desc': desc})

def races_index(request):
  response=requests.get('https://www.dnd5eapi.co/api/races').json()
  print(response)
  return render(request, 'characters/races_index.html', {'response':response})

def race(request, race_name):
  race_name = race_name.lower().replace(" ", "-")
  response=requests.get(f'https://www.dnd5eapi.co/api/races/{race_name}').json()
  print(response)
  name = response.get('name', '')
  align = response.get('alignment', '')
  lang = response.get('language_desc', '')
  traits = response.get('traits', '')

  return render(request, 'characters/race.html', {'name': name, 'align': align, 'lang': lang, 'traits': traits })