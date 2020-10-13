from django.core.management.base import BaseCommand
import json
from library.models import Book

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('library/management/commands/booklist.json', 'r') as books_json:
            text = books_json.read()
        books = json.loads(text)
        for book in books['books']:
            author = book['author']
            title = book['title']
            image = book['image']
            year = book['year']
            pages = book['pages']
            url = book['url']
            country = book['country']
            language = book['language']

            output_book = Book(author=author, title=title, image=image, year=year, pages=pages, url=url, country=country, language=language)
            output_book.save()
    
            
