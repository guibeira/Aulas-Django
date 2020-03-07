from django import forms
from .models import Pet


class PetForm(forms.ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.upper() == 'PUTINHO':
            raise forms.ValidationError("Nome muito ofensivo  ¯\_₍⸍⸌̣ʷ̣̫⸍̣⸌₎_/¯ !!!")
        return nome
    
    class Meta:
        model = Pet 
        fields = '__all__'