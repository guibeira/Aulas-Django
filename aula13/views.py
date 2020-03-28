from django.shortcuts import render
from .forms import UploadFileForm, UploadFileModelForm
from .models import UploadFile
# Create your views here.
from django.conf import settings
import os


def aula13(request):
    form = UploadFileForm()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

    contexto = {
        "form": form,
    }
    return render(request, 'aula13/aula13.html', context=contexto)


def aula13_com_model_form(request):
    form = UploadFileModelForm()
    if request.method == "POST":
        form = UploadFileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    files = UploadFile.objects.all()
    contexto = {
        "form": form,
        "files": files,
    }
    return render(request, 'aula13/aula13.html', context=contexto)


def handle_uploaded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

