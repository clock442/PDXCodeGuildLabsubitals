from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    year = models.IntegerField()
    pages = models.IntegerField()
    url = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ', ' + self.author