from django.shortcuts import render

# Create your views here.


def mostra_arquivo_estatico(request):
    return render(request, "aula10/aula10.html", {"titulo": "Titulo do meu site"})