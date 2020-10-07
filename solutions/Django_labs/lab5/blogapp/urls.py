from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_vue, name='login'),
    path('profile/', views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)