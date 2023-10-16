from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    avatar = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_id': self.id})
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    picURL = models.CharField(max_length=500)
    race = models.CharField(max_length=20)
    alignment = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=1)
    strength = models.IntegerField
    constitution = models.IntegerField
    dexterity = models.IntegerField
    charisma = models.IntegerField
    wisdom = models.IntegerField
    intelligence = models.IntegerField

    # User foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.id})'

