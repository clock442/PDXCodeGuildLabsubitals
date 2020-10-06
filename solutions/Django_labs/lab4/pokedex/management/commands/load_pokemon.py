from django.core.management.base import BaseCommand
import json
from pokedex.models import Pokemon, PokemonType

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('pokedex/management/commands/pokemon.json', 'r') as poketext:
            pokejson = poketext.read()
        pokedata = json.loads(pokejson)
        for pokemon_data in pokedata['pokemon']:
            number = pokemon_data['number']
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            image_front = pokemon_data['image_front']
            image_back = pokemon_data['image_back']
            type_names = pokemon_data['types']

            pokemon = Pokemon(number=number, name=name, height=height, weight=weight, image_front=image_front, image_back=image_back)
            pokemon.save()

            for type_name in type_names:
                pokemon_type, created = PokemonType.objects.get_or_create(
                    name=type_name
                )
                pokemon.types.add([pokemon_type])

            pokemon.save()