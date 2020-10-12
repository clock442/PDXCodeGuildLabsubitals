from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import BlogPost

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body', 'image', 'public']

