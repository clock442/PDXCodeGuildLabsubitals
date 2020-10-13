from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, 'library/index.html')

def books(request):
    books = Book.objects.all()
    data = []
    for book in books:
        data.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'image': book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language
        })

    return JsonResponse({'books': data})


def search(request):
    text = request.GET['text']
    print(text)
    books = Book.objects.all()
    search_books = books.filter(Q(title__icontains=text) | Q(author__icontains=text))
    data = []
    for book in search_books:
        data.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'image': book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language
        })



    return JsonResponse({'search_books': data})
