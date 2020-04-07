from django.contrib import admin
from django.urls import path
from .views import  cadastro
from .views import novo_cadastro
from  .views import atualizar_cadastro
from .views import apagar_cadastro

urlpatterns = [
    path('list/', cadastro, name="lista"),
    path('novo/', novo_cadastro, name="novo"),
    path('atualizar/<int:id>/', atualizar_cadastro, name="atualizar"),
    path('apagar/<int:id>/', apagar_cadastro, name="apagar"),


]