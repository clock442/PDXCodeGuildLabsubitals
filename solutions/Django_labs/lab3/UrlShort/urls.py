from django.urls import path
from . import views

app_name = 'urlshort'
urlpatterns= [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('<str:input_code>/', views.redirect_view, name='redirect_view'),
    path('delete/<int:url_item_id>/', views.delete, name='delete'),
]