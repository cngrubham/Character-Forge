from django.forms import ModelForm
from .models import Character
from django import forms
import requests

GENDER_CHOICES = (
    ('Dragonborn-M', 'Dragonborn-M'),
    ('Dragonborn-F', 'Dragonborn-F'),
    ('Dwarf-M', 'Dwarf-M'),
    ('Dwarf-F', 'Dwarf-F'),
    ('Elf-M', 'Elf-M'),
    ('Elf-F', 'Elf-F'),
    ('Gnome-M', 'Gnome-M'),
    ('Gnome-F', 'Gnome-F'),
    ('Half-elf-M', 'Half-elf-M'),
    ('Half-elf-F', 'Half-elf-F'),
    ('Half-orc-M', 'Half-orc-M'),
    ('Half-orc-F', 'Half-orc-F'),
    ('Halfling-M', 'Halfling-M'),
    ('Halfling-F', 'Halfling-F'),
    ('Human-M', 'Human-M'),
    ('Human-F', 'Human-F'),
    ('Tiefling-M', 'Tiefling-M'),
    ('Tiefling-F', 'Tiefling-F'),
)




class CharacterForm(ModelForm):
  gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select)
  race = forms.ChoiceField(widget=forms.Select)
  alignment = forms.ChoiceField(widget=forms.Select)
  class Meta:
      model = Character
      fields = ['name', 'gender', 'race', 'alignment', 'level', 'exp']

  def __init__(self, *args, **kwargs):
      super(CharacterForm, self).__init__(*args, **kwargs)

      # Fetch race choices from the API
      response = requests.get('https://www.dnd5eapi.co/api/races').json()
      races = [(race['name'], race['name']) for race in response.get('results', [])]
      
      response = requests.get('https://www.dnd5eapi.co/api/alignments').json()
      alignments = [(alignment['name'], alignment['name']) for alignment in response.get('results', [])]
      # Set the choices for the 'race' field
      self.fields['race'].choices = races
      self.fields['alignment'].choices = alignments