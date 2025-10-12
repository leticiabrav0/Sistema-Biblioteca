from django.urls import path
from app_biblioteca import views

urlpatterns = [
    #rota, view, nome de referencia
    path('', views.home, name='home'),
    #path('usuarios/', views.usuario, name='listagem_usuarios'),
    path('livros/', views.livro_list, name='livro_list'),
    #path('livros/create/', views.livro_create, name='livro_create'),
]
