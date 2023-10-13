from django.forms import ModelForm
from .models import User, Character

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['name', 'email', 'password']

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = ['name', 'alignment', 'exp', 'level']