
# Register your models here.
from django.contrib import admin
# import your models here
from .models import User
from .models import Character

# Register your models here
admin.site.register(User)
admin.site.register(Character)
