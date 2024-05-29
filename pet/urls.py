from django.urls import path
from pet import views
from register.views import register

urlpatterns = [
    path('', views.readall, name='index'),  # Rota para a página inicial
    path('create/', views.create, name='Criar'),
    path('read/<int:id_animal>/', views.read, name='Ler'),  # Adicionando a rota para os detalhes do animal
    path('update/<int:id_animal>/', views.update, name='Atualizar'),
    path('delete/<int:id_animal>/', views.delete, name='Deletar'),
    path('delete/confirm/<int:id_animal>/', views.confirmdelete, name='pet_confirm_delete'),
    path('register/', register, name='register'),  # Rota para o registro de usuário
]