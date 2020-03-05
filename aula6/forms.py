from django import forms
from aula5.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ("data_nascimento",)
