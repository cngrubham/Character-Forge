from django.shortcuts import render
import requests


# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

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