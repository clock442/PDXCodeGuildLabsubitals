from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('search/', views.search, name='search'),
]