from django.shortcuts import render

# Create your views here.

def index9(request):
    return render(request, "aula9/aula9.html", {"nome": "Guilherme"})