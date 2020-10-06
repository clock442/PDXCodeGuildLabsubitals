from django.db import models

class PokemonType(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=300)
    image_back = models.CharField(max_length=300)
    types = models.ManyToManyField(PokemonType, related_name='pokemons_many')
    def __str__(self):
        return self.name