from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import views
from .models import Character, User, FACTION_URLS
from .forms import CharacterForm, UserForm
from django.urls import reverse, reverse_lazy
import requests
import random
from django.http import JsonResponse



GENDER_IMAGE_URLS = {
    'Dragonborn-M': 'images/dragonborn.png',
    'Dragonborn-F': 'images/dragonborn-female.jpeg',
    'Dwarf-M': 'images/Dwarf.webp',
    'Dwarf-F': 'images/dwarf-female.png',
    'Elf-M': 'images/elf-male.webp',
    'Elf-F': 'images/elf.png',
    'Gnome-M': 'images/gnome.webp',
    'Gnome-F': 'images/gnome-female.jpeg',
    'Half-elf-M': 'images/half-elf-male.png',
    'Half-elf-F': 'images/half-elf.jpeg',
    'Half-orc-M': 'images/Half_Orc_male.webp',
    'Half-orc-F': 'images/half-orc-female.jpeg',
    'Halfling-M': 'images/halfling-male.png',
    'Halfling-F': 'images/halfling_female.jpeg',
    'Human-M': 'images/human_male.jpeg',
    'Human-F': 'images/human-female.png',
    'Tiefling-M': 'images/tiefling-male.jpeg',
    'Tiefling-F': 'images/tiefling-female.jpeg',
}

def proxy_api(request, alignment_name):
    # Construct the URL for the external API
    api_url = f'https://www.dnd5eapi.co/api/alignments/{alignment_name}'
    
    # Make a request to the external API
    response = request.get(api_url)
    data = response.json()

    return JsonResponse(data)

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
    avatar_value = user.avatar
    avatar_result = [ (a, u) for a, u in FACTION_URLS if a == avatar_value]

    character_form = CharacterForm()
    # will probably need to change.all to display only specific user characters
    return render(request, 'user/user_detail.html', {'character_form': character_form, 'user': user, 'user_id': user_id, 'avatar_name': avatar_result[0][0], 'avatar_url': avatar_result[0][1]})


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

  def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['faction_urls'] = FACTION_URLS
        return context

class UserDelete(DeleteView):
  model = User
  success_url = reverse_lazy('user_index')



def character_create(request, user_id, character_id=None):
    if character_id is not None:
        # Fetch the character to edit
        character = Character.objects.get(id=character_id)
        if request.method == 'POST':
            form = CharacterForm(request.POST, instance=character)
            if form.is_valid():
                form.save()
                return redirect('user_detail', user_id=user_id)
        else:
            form = CharacterForm(instance=character)

    else:
        if request.method == 'POST':
            form = CharacterForm(request.POST)
            if form.is_valid():
                new_character = form.save(commit=False)
                new_character.user_id = user_id
                selected_gender = form.cleaned_data.get('gender')
                gender_image_url = GENDER_IMAGE_URLS.get(selected_gender, 'URL_FOR_DEFAULT_IMAGE')
                new_character.picURL = gender_image_url

                # Generate random stats here
                new_character.strength = random.randint(8, 20)
                new_character.constitution = random.randint(8, 20)
                new_character.dexterity = random.randint(8, 20)
                new_character.charisma = random.randint(8, 20)
                new_character.wisdom = random.randint(8, 20)
                new_character.intelligence = random.randint(8, 20)

                new_character.save()
                print("Character creation successful")
                return redirect('user_detail', user_id=user_id)
            else:
                print("Form is invalid")
        else:
            form = CharacterForm()

    # Fetch race choices from the API
    response = requests.get('https://www.dnd5eapi.co/api/races').json()
    races = [(race['name'], race['name']) for race in response.get('results', [])]

    # Include character_id and race choices in the context dictionary
    context = {'form': form, 'user_id': user_id, 'character_id': character_id, 'races': races}

    return render(request, 'main_app/character_form.html', context)


class CharacterDelete(DeleteView):
  model = Character
  template_name = 'main_app/character_confirm_delete.html'
  success_url = reverse_lazy('user_index')

class CharacterUpdate(UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'main_app/character_form.html'  # The HTML template for editing characters
    context_object_name = 'character'  # The variable name used in the template
    pk_url_kwarg = 'character_id'  # Specify the URL parameter name for character_id

    # Define the success URL after updating a character
    def get_success_url(self):
        character_id = self.kwargs.get('character_id')
        return reverse('detail', kwargs={'character_id': character_id})

def character_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  form = CharacterForm()
  character_race_case_sensitive = character.race
  return render(request, 'character/detail.html', {'character': character, 'form': form, 'character_race_case_sensitive': character_race_case_sensitive})




