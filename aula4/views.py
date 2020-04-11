from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


def index(request):
    context = {"alunos": ["joao", "maria", "josé", "pedro",]}
    return render(request, "aula4/index.html", context=context)
