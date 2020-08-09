from django.contrib import admin
from .models import About, Experience, Education, Interest, Skill

# Register your models here.


myModels = [About, Experience, Education, Interest, Skill]
admin.site.register(myModels)
