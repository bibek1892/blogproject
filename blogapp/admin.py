from django.contrib import admin
from .models import *
# admin.site.register(Blog) #to register the class after making dbms class at models.py

# admin.site.register(Event)

# admin.site.register(Catagory)

# admin.site.register(News)

admin.site.register([Blog, Event, Catagory, News, Message])
