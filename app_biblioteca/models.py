from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Classe feita para estudo, não utilizada no projeto
# class Usuario(models.Model):
    # id_usuario = models.AutoField(primary_key=True)
    # nome_usuario = models.TextField(max_length=150)
    # senha_usuario = models.TextField(max_length=100)

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
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.usuario} - {self.livro}'