from django.db import models
from django.urls import reverse

# Create your models here.

FACTION_CHOICES = (
    ('Harpers', 'Harpers'),
    ('Order of the Gauntlet', 'Order of the Gauntlet'),
    ('Emerald Enclave', 'Emerald Enclave'),
    ('Lord''s Alliance', 'Lord''s Alliance'),
    ('Zhentarim', 'Zhentarim')
)

FACTION_URLS = (
    ('Harpers', 'https://www.dndbeyond.com/avatars/thumbnails/6/340/420/618/636272677995471928.png'),
    ('Order of the Gauntlet', 'https://www.dndbeyond.com/attachments/thumbnails/5/928/290/504/br-orderofthegauntlet.png'),
    ('Emerald Enclave', 'https://www.dndbeyond.com/attachments/thumbnails/5/925/290/504/br-emeraldenclave.png'),
    ('Lord''s Alliance', 'https://www.dndbeyond.com/attachments/thumbnails/5/926/290/504/br-lordsalliance.png'),
    ('Zhentarim', 'https://www.dndbeyond.com/attachments/thumbnails/5/927/290/504/br-zhentarim.png')
)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    avatar = models.CharField(
        max_length=25,
        choices=FACTION_CHOICES,
        default=FACTION_CHOICES[0][0])
    
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

