# app_biblioteca/views.py

from django.shortcuts import render, redirect
# Funções de autenticação que vamos usar
from django.contrib.auth import authenticate, login, logout
# Decorador para proteger páginas
from django.contrib.auth.decorators import login_required
from .models import Livro, Emprestimo
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

def login_view(request):
    # Se o usuário já estiver logado, redireciona para a home
    if request.user.is_authenticated:
        return redirect('home')

    # Se o formulário foi enviado (método POST)
    if request.method == 'POST':
        # Pega o 'username' e a 'password' do formulário
        nome_usuario = request.POST.get('username')
        senha_usuario = request.POST.get('password')

        # O Django verifica se o usuário existe e se a senha está correta
        user = authenticate(request, username=nome_usuario, password=senha_usuario)

        if user is not None:
            # Se o usuário é válido, inicia a sessão (faz o login)
            login(request, user)
            return redirect('home') # Redireciona para a página principal após o login
        else:
            # Se for inválido, renderiza a página de login novamente com uma mensagem de erro
            contexto = {'error': 'Usuário ou senha inválidos'}
            return render(request, 'login.html', contexto)

    # Se for o primeiro acesso à página (método GET), apenas mostra o formulário
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login') # Redireciona para a tela de login após o logout


# Esta será a página principal para usuários logados
@login_required(login_url='login') # Se tentar acessar sem estar logado, redireciona para a URL de nome 'login'
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def listar_livros(request):
    # 1. Busca todos os objetos Livro no banco de dados, ordenados por título
    livros = Livro.objects.all().order_by('titulo')
    
    # 2. Cria um "contexto" (um dicionário) para enviar os dados para o template
    contexto = {
        'livros': livros
    }
    
    # 3. Renderiza o template 'livros/livros.html' e passa o contexto para ele
    return render(request, 'livros/livros.html', contexto)

@require_POST  # Garante que esta view só aceite requisições POST
@login_required(login_url='login') # Garante que o usuário esteja logado
def registrar_emprestimo(request, livro_id):

    # 1. Busca o livro pelo ID. Se não encontrar, retorna "Página não encontrada"
    livro = get_object_or_404(Livro, id=livro_id)

    # 2. Pega o usuário que está logado
    usuario = request.user

    # 3. VERIFICAÇÃO: Checa se o livro tem estoque
    if livro.estoque > 0:

        # 4. Diminui o estoque e salva o livro
        livro.estoque -= 1
        livro.save()

        # 5. Define a data de devolução (ex: 7 dias a partir de hoje)
        data_prevista = timezone.now().date() + timedelta(days=7)

        # 6. Cria o novo registro de Empréstimo no banco de dados
        Emprestimo.objects.create(
            livro=livro,
            usuario=usuario,
            data_devolucao_prevista=data_prevista
        )

        messages.success(
            request,
            f'O livro "{livro.titulo}" foi emprestado com sucesso! '
            f'Deve ser devolvido até {data_prevista.strftime("%d/%m/%Y")}.'
        )


    else:
        messages.error(
            request,
            f'O livro "{livro.titulo}" não está disponível no momento (sem estoque).'
        )
        pass

    # 7. Redireciona o usuário de volta para a lista de livros
    return redirect('listar_livros')

@login_required(login_url='login')
def listar_emprestimos_ativos(request):
    # TODO: Futuramente, esta página será restrita somente para Funcionários. Mas, por enquanto, qualquer usuário logado pode ver.
    
    # 1. Busca todos os Emprestimos onde a data_devolucao É NULA (isnull=True)
    # e ordena pela data de devolução prevista.
    emprestimos_ativos = Emprestimo.objects.filter(
        data_devolucao__isnull=True
    ).order_by('data_devolucao_prevista')
    
    contexto = {
        'emprestimos': emprestimos_ativos
    }
    
    # TODO: 2. Renderiza um NOVO template que ainda será criado 
    return render(request, 'emprestimos/listar_ativos.html', contexto)