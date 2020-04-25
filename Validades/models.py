from django.db import models

class Cadastro(models.Model):
    Produto = models.CharField(max_length=40)
    Fornecedor = models.CharField(max_length=20)
    Quantidade = models.IntegerField()
    Data_do_Registro = models.DateField()
    Validade = models.DateField()


    def __str__(self):
        return self.Produto + ' : ' + self.Fornecedor
