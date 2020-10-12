from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, LoginForm, BlogPostForm
from .models import User, BlogPost
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
    print(request.user.id)

    posts = request.user.users.all()
    print(posts[3].image)
    print(posts[1])
    print(posts)
    print(posts[1].id)

    context = {
        'posts': posts,
    }

    return render(request, 'blogapp/profile.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()


            return HttpResponseRedirect(reverse('blogapp:profile'))
        
    else:
        form = BlogPostForm()

    return render(request, 'blogapp/create.html', {'form': form})

@login_required
def edit(request, post_id):
    print(post_id)
    post_object = get_object_or_404(BlogPost, id=post_id, user=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogapp:profile'))
    
    else:
        form = BlogPostForm(instance=post_object)

    context = {
        'form': form
    }
    return render(request, 'blogapp/edit.html', context)

