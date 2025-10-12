# projeto_biblioteca/urls.py

from django.contrib import admin
from django.urls import path, include # A palavra 'include' é a chave aqui

urlpatterns = [
    path('admin/', admin.site.urls),

    # Esta linha diz: "Para qualquer rota que não seja '/admin/', 
    # vá procurar as respostas no arquivo urls.py de app_biblioteca"
    path('', include('app_biblioteca.urls')),
]