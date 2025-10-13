from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Autor, Livro, Emprestimo

# --- CLASSE DE CUSTOMIZAÇÃO PARA LIVROS ---
class LivroAdmin(admin.ModelAdmin):
    # A linha abaixo diz ao admin para mostrar esses campos na tela de listagem
    list_display = ('titulo', 'autor', 'estoque')

admin.site.register(Usuario, UserAdmin)
admin.site.register(Autor)
admin.site.register(Emprestimo)

# A linha abaixo "conecta" o modelo Livro com sua classe de customização
admin.site.register(Livro, LivroAdmin)