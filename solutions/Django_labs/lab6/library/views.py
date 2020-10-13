from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, 'library/index.html')

def books(request):
    book_list = Book.objects.order_by('year')
    paginator = Paginator(book_list, 5)
    page = request.GET.get('page')
    books = paginator.page(page)
    pag_pages = paginator.num_pages
    data = []
    for book in books:
        data.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'image': 'https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/4%20Django/labs/images/' + book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language
        })

    return JsonResponse({'books': data, 'pag_pages': pag_pages})


def search(request):
    text = request.GET['text']
    books = Book.objects.order_by('year')
    search_books = books.filter(Q(title__icontains=text) | Q(author__icontains=text))
    paginator = Paginator(search_books, 5)
    page = request.GET.get('page')
    books = paginator.page(page)
    pag_pages = paginator.num_pages
    data = []
    for book in books:
        data.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'image': 'https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/4%20Django/labs/images/' + book.image,
            'year': book.year,
            'pages': book.pages,
            'url': book.url,
            'country': book.country,
            'language': book.language
        })


    return JsonResponse({'search_books': data, 'pag_pages': pag_pages})
