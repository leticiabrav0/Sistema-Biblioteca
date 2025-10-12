from django.shortcuts import render, redirect
from .models import Usuario, Livro, Autor, Emprestimo
# from .forms import LivroForm, AutorForm, EmprestimoForm

def home(request):
    return render(request, 'home.html')

#def usuario(request):
#    # Salvar os dados da tela no Banco de Dados
#    novo_usuario = Usuario()
#    novo_usuario.nome_usuario = request.POST.get('nome_usuario')
#    novo_usuario.senha_usuario = request.POST.get('senha_usuario')
#    novo_usuario.save()
#
#    # Exibir usuários cadastrados em uma nova página
#    usuarios = {
#        'usuarios': Usuario.objects.all()
#    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livro_list.html', {'livros': livros})

#def livro_create(request):
#    if request.method == 'POST':
#        form = LivroForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('livro_list')
#    else:
#        form = LivroForm()
#    return render(request, 'livro_form.html', {'form': form})