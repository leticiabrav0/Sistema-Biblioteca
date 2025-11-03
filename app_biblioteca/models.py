from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class Usuario(AbstractUser):
    pass 


class Autor(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.PositiveIntegerField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_prevista = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.usuario.username} - {self.livro.titulo}'