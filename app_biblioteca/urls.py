# app_biblioteca/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('livros/', views.listar_livros, name='listar_livros'),
    path('emprestar/<int:livro_id>/', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('emprestimos/', views.listar_emprestimos_ativos, name='listar_emprestimos_ativos'),
    path('devolver/<int:emprestimo_id>', views.registrar_devolucao, name='registrar_devolucao'),
]