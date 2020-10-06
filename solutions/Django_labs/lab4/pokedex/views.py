from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pokemon, PokemonType
from django.db.models import Q



def index(request):
    pokemons = Pokemon.objects.all()
    search_pokemon = request.GET.get('search_pokemon', '')
    if search_pokemon != '':
        pokemons = pokemons.filter(Q(name__icontains=search_pokemon)
                                    | Q(number__icontains=search_pokemon)
                                    | Q(height__icontains=search_pokemon))

    context = {
        'pokemons': pokemons,
    }
    return render(request, 'pokedex/index.html', context)


def info(request, pokemon_name):
    poke_info = request.GET['pokemon_name']
    poke_name = poke_info.name
    poke_number = poke_info.number
    poke_height = poke_info.height
    poke_weight = poke_info.weight
    poke_front_img = poke_info.image_front
    poke_back_img = poke_info.image_back
    

    context = {
        'poke_name': poke_name,
        'poke_number': poke_number,
        'poke_height': poke_height,
        'poke_weight': poke_weight,
        'poke_front_img': poke_front_img,
        'poke_back_img': poke_back_img,

    }
    return render(request, 'pokedex/info.html', context)



