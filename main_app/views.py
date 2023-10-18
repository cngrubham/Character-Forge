from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character, User
from .forms import CharacterForm
from django.urls import reverse, reverse_lazy
import requests
import random




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

class UserCreate(CreateView):
    model = User
    fields = '__all__'
   
class UserUpdate(UpdateView):
  model = User
  fields = '__all__'

class UserDelete(DeleteView):
  model = User
  success_url = reverse_lazy('user_index')


def character_create(request, user_id):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.race = form.cleaned_data['race']
            character.user_id = user_id
            print("Form is valid")
            character.save()
            return redirect('detail', character_id=character.id)
    else:
        form = CharacterForm()

    return render(request, 'main_app/character_form.html', {'form': form, 'user_id': user_id})



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
  form = CharacterForm()
  return render(request, 'character/detail.html', {'character': character, 'form': form})


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
