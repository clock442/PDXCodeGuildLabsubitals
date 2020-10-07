from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<str:pokemon_name>/', views.info, name='info')
]