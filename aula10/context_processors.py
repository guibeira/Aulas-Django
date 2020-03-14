from aula8.models import Pet
from django.utils import timezone


def total_pets(request):
    total = Pet.objects.all().count()
    return {"total_pet": total}


def data_requisicao(request):
    return {"data_requisicao": timezone.now()}