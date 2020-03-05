from django.shortcuts import render, get_object_or_404
from aula5.models import Contato
from .forms import ContatoForm


def index(request):
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
    contatos = Contato.objects.all()
    contexto = {
        "form": form,
        "contatos": contatos
    }
    return render(request, 'aula6/index.html', context=contexto)


def editar_contato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    contatos = Contato.objects.all()
    form = ContatoForm(initial={"nome":contato.nome, "email":contato.email, "twitter":contato.twitter})
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
    contexto = {
        "form": form,
        "contatos": contatos
    }
    return render(request, 'aula6/index.html', context=contexto)