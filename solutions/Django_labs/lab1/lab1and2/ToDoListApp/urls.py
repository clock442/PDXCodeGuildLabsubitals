from django.urls import path
from . import views
app_name = 'ToDoListApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('addcontact/', views.addContact, name='addContact'),
]
