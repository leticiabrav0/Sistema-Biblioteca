# app_biblioteca/views.py

from django.shortcuts import render, redirect
# Funções de autenticação que vamos usar
from django.contrib.auth import authenticate, login, logout
# Decorador para proteger páginas
from django.contrib.auth.decorators import login_required

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