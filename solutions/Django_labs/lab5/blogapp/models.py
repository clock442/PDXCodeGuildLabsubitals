from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # retype_password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='../uploaded_files/images/kitten150x100.jpg')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title 