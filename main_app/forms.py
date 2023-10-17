from django.forms import ModelForm, forms
from .models import Character, User, FACTION_CHOICES
from django.forms.widgets import Select

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = ['name', 'race', 'alignment', 'level', 'exp']

# Create ModelForm for use in UserCreate route
class UserForm(ModelForm):
  class Meta:
    model = User
    fields = "__all__"
    widgets = {
      'avatar': Select(choices=FACTION_CHOICES)
    }
   