from django import forms
from aula5.models import Contato


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=30)
    email = forms.EmailField()
    twitter = forms.URLField()

    def save(self, instance=None):
        if isinstance is None:
            nome = self.cleaned_data['nome']
            email = self.cleaned_data['email']
            twitter = self.cleaned_data['twitter']
            contato = Contato(nome=nome, email=email, twitter=twitter)
            contato.save()
        else:
            instance.nome = self.cleaned_data['nome']
            instance.email = self.cleaned_data['email']
            instance.twitter = self.cleaned_data['twitter']
            instance.save()