from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    print(request)
    return HttpResponse('Hello World')

def addContact(request):
    return HttpResponse('hello')