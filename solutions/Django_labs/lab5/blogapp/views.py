from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
import django.contrib.auth
import requests
from lab5 import local_settings

def index(request):

    return render(request, 'blogapp/index.html')

def register(request):
    if request.method == 'POST':
        # form = UserForm(request.POST)

        recaptcha_data = {
            'response': request.POST['g-recaptcha-response'],
            'secret': local_settings.recaptcha_secret_key
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)

        
        if (response.json()['success'] == False):
            message = 'failed_recaptcha'
            return render(request, 'blogapp/register.html', {'message': message})
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # retype_password = request.POST['retype_password']

        # if password != retype_password:
        #     message = 'passwords_dont_match'
        #     return render(request, 'blogapp/register.html', {'message': message})

        if User.objects.filter(username=username).exists():
            message = 'user_exists'
            return render(request, 'blogapp/register.html', {'message': message})

        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('blogapp:index'))

    else:
        form = UserForm()
    return render(request, 'blogapp/register.html', {'form': form})

def login_vue(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is None:
            message = 'not_found'
        else:
            django.contrib.auth.login(request, user)
            next = request.GET.get('next', reverse('blogapp:index'))
            return HttpResponseRedirect(next)





    else:
        form = LoginForm()

    return render(request, 'blogapp/login.html', {'form': form, 'message': message})

@login_required
def profile(request):
    print(request)

    return render(request, 'blogapp/profile.html')
