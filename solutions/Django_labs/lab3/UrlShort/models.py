from django.db import models

class ShortendURL(models.Model):
    code = models.CharField(max_length=200)
    url = models.URLField()
    def __str__(self):
        return self.url
