from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Cadastro
from .forms import CadastroForm

# Create your views here.
@login_required
def cadastro(request):
    registro = Cadastro.objects.all()
    return render(request, 'lista.html', {'registro':registro})
@login_required
def novo_cadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return  render(request, 'formulario.html', {'form': form})

@login_required
def atualizar_cadastro(request, id):
    cadastro = get_object_or_404(Cadastro, pk=id)
    form = CadastroForm(request.POST or None, request.FILES or None, instance=cadastro)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'formulario.html', {'form': form})

@login_required
def apagar_cadastro(request,id):
    cadastro = get_object_or_404(Cadastro, pk=id)
    form = CadastroForm(request.POST or None, request.FILES or None, instance=cadastro)

    if request.method == 'POST':
        cadastro.delete()
        return redirect('lista')
    return render(request, 'confirma_delete.html', {'cadastro': cadastro})