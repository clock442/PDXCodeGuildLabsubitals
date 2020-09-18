from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

# Create your views here.
def primary(request):
    blog_posts = MyModel.objects.order_by('date_published')
    context = {
        'blog_posts': blog_posts 
    }
    return render(request, 'myapp/primary.html', context)