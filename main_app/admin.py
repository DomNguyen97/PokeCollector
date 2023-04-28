from django.contrib import admin
from .models import Pokemon, Move, Item

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Move)
admin.site.register(Item)