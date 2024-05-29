from django.urls import path
from register.views import register, index  # Importe a view index
from django.contrib import admin
from register import views

urlpatterns = [
    path('register/', register, name='register'),
    path('', index, name='index'),  # Adicione a URL para a view index
    path('login/', views.login_view, name='login'),
]