from django.forms import ModelForm
from .models import Character
from django import forms

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

class CharacterForm(ModelForm):
  race = forms.ChoiceField(choices=RACE_CHOICES, widget=forms.Select)
  class Meta:
    model = Character
    fields = ['name', 'race', 'alignment', 'level', 'exp']
   