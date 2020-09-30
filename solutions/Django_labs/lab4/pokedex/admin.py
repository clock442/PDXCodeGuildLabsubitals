from django.contrib import admin
from .models import PokemonType, Pokemon

admin.site.register(Pokemon)
admin.site.register(PokemonType)