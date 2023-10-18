from django.forms import ModelForm
from .models import Character
from django import forms

RACE_CHOICES = (
    ('images/dragonborn.png', 'Dragonborn-M'),
    ('images/dragonborn-female.jpeg', 'Dragonborn-F'),
    ('images/Dwarf.webp', 'Dwarf-M'),
    ('images/dwarf-female.png', 'Dwarf-F'),
    ('images/elf-male.webp', 'Elf-M'),
    ('images/elf.png', 'Elf-F'),
    ('images/gnome.webp', 'Gnome-M'),
    ('images/gnome-female.jpeg', 'Gnome-F'),
    ('images/half-elf.jpeg', 'Half-elf-M'),
    ('images/half-elf.jpeg', 'Half-elf-F'),
    ('images/Half_Orc_male.webp', 'Half-orc-M'),
    ('images/half-orc-female.jpeg', 'Half-orc-F'),
    ('images/halfling-male.png', 'Halfling-M'),
    ('images/halfling_female.jpeg', 'Halfling-F'),
    ('images/human_male.jpeg', 'Human-M'),
    ('images/human-female.png', 'Human-F'),
    ('images/tiefling-male.jpeg', 'Tiefling-M'),
    ('images/tiefling-female.jpeg', 'Tiefling-F'),
)



class CharacterForm(ModelForm):
  # race = forms.ChoiceField(choices=RACE_CHOICES, widget=forms.Select)
  class Meta:
    model = Character
    fields = ['name', 'alignment', 'level', 'exp']
    # 'race', DONT FORGET TO ADD RACE FIELD BACK IN
   