from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('primary/', views.primary, name='primary')
]