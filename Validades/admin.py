from django.contrib import admin
from .models import Cadastro
# Register your models here.
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('Produto', 'Fornecedor', 'Validade')


admin.site.register(Cadastro, CadastroAdmin)