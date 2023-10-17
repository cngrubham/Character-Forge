from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import views
from .models import Character, User, FACTION_URLS
from .forms import CharacterForm, UserForm
from django.urls import reverse, reverse_lazy
import requests
import random

RACE_CHOICES = (
    ('Dragonborn', 'https://www.dndbeyond.com/avatars/thumbnails/6/340/420/618/636272677995471928.png'),
    ('Dwarf', 'https://www.dndbeyond.com/avatars/thumbnails/6/254/420/618/636271781394265550.png'),
    ('Elf', 'https://www.dndbeyond.com/avatars/thumbnails/7/639/420/618/636287075350739045.png'),
    ('Gnome', 'https://www.dndbeyond.com/avatars/thumbnails/6/334/420/618/636272671553055253.png'),
    ('Half-elf', 'https://www.dndbeyond.com/avatars/thumbnails/6/481/420/618/636274618102950794.png'),
    ('Half-orc', 'https://www.dndbeyond.com/avatars/thumbnails/6/466/420/618/636274570630462055.png'),
    ('Halfling', 'https://www.dndbeyond.com/avatars/thumbnails/6/256/420/618/636271789409776659.png'),
    ('Human', 'https://www.dndbeyond.com/avatars/thumbnails/6/258/420/618/636271801914013762.png'),
    ('Tiefling', 'https://www.dndbeyond.com/avatars/thumbnails/7/641/420/618/636287076637981942.png'),
)

def dice_roll():
    return random.randint(8, 20)

# Define the home view
def home(request):
  return render(request, 'home.html')

def user_login(request):
    return render(request, 'user/login.html')

def user_index(request):
    users = User.objects.all()
    return render(request, 'user/user_index.html', {'users': users})

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    character_form = CharacterForm()
    # will probably need to change.all to display only specific user characters
    return render(request, 'user/user_detail.html', {'character_form': character_form, 'user': user})

# class UserCreate(views.View):
#     template_name = 'user/user_create.html'
#     get(req, res)

class UserCreate(CreateView):
    # Trying to set model attribute to UserForm ModelForm,
    # instead of User model.
    model = User
    form_class = UserForm
    # fields = '__all__'
    template_name = 'main_app/user_form.html'
    # success_url = ''

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['faction_urls'] = FACTION_URLS
        return context

    # def form_valid(self, form):
    #   form.save()
    #   return super().form_valid(form)

    def get_success_url(self):
       return reverse('user_detail', args=[self.object.id])
   
class UserUpdate(UpdateView):
  model = User
  fields = '__all__'

class UserDelete(DeleteView):
  model = User
  success_url = reverse_lazy('user_index')


def character_create(request, user_id):
    form = CharacterForm(request.POST)
    if form.is_valid():
      new_character = form.save(commit=False)
      new_character.user_id = user_id
      new_character.save()
    return redirect('user_detail', user_id=user_id)


    #   race = form.get('race')
    #   picture_url = [url for name, url in RACE_CHOICES if name == race]
    #   if picture_url:
    #         picture_url = picture_url[0]  
    #   else:
    #       picture_url = 'URL_FOR_DEFAULT_IMAGE'
        
    #   form.instance.picURL = picture_url
        
    #     # dice roll stats, may need to change how this is implemented
    #   form.instance.strength = dice_roll()
    #   form.instance.constitution = dice_roll()
    #   form.instance.dexterity = dice_roll()
    #   form.instance.charisma = dice_roll()
    #   form.instance.wisdom = dice_roll()
    #   form.instance.intelligence = dice_roll()

    #   return super().form_valid(form)

    # def get_success_url(self):
    #         return reverse('user_detail')

class CharacterDelete(DeleteView):
  model = Character
  success_url = 'user/user_detail'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'alignment', 'experience', 'level']

def character_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  return render(request, 'character/detail.html', {'character': character})


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

# def race(request, race_name):
#   race_name = race_name.lower().replace(" ", "-")
#   response=requests.get(f'https://www.dnd5eapi.co/api/races/{race_name}').json()
#   print(response)
#   name = response.get('name', '')
#   align = response.get('alignment', '')
#   lang = response.get('language_desc', '')
#   traits = response.get('traits', '')

#   return render(request, 'characters/race.html', {'name': name, 'align': align, 'lang': lang, 'traits': traits })

def race(request, race_name):
    race_name = race_name.lower().replace(" ", "-")
    picture_url = [url for name, url in RACE_CHOICES if name == race_name]
    if picture_url:
        picture_url = picture_url[0]  
    else:
        # default if none found
        picture_url = 'URL_FOR_DEFAULT_IMAGE'
    
    response = requests.get(f'https://www.dnd5eapi.co/api/races/{race_name}').json()
    api_race_name = response.get('name', '')
    align = response.get('alignment', '')
    lang = response.get('language_desc', '')
    traits = response.get('traits', '')

    return render(request, 'characters/race.html', {'name': api_race_name, 'align': align, 'lang': lang, 'traits': traits, 'picture_url': picture_url})
