from django.utils import timezone

from aula8.models import Pet


def total_pets(request):
    total = Pet.objects.all().count()
    return {"total_pet": total}


def data_requisicao(request):
    return {"data_requisicao": timezone.now()}
