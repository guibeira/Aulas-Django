from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60, widget=forms.widgets.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username):
            raise forms.ValidationError("Esse usuário não existe")
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Senha inválida")
        return password

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)
