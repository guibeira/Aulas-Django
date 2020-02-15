from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

def index(request):
    html = f"<h1>Bem vindo à </h1>"
    response = HttpResponse(html, status=404)
    response['ultimo_acesso'] = timezone.localtime(timezone.now())
    return response


def setacookie(request):
    response = HttpResponse()
    response.set_cookie("my_name", value="Guilherme")

    return response


def redireciona(request):
    return HttpResponseRedirect('https://uol.com.br')