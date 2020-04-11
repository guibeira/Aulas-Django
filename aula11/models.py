from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .managers import CustomPostManager, TecPostManager


class SoftDelete(models.Model):
    deletado_em = models.DateTimeField(null=True)
    deletado = models.BooleanField(default=False)

    def delete(self):
        self.deletado = True
        self.deletado_em = timezone.now()
        self.save()

    class Meta:
        abstract = True

        
class Auditoria(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categoria(Auditoria):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


class Post(Auditoria, SoftDelete):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    objects = CustomPostManager()

    def __str__(self):
        return self.title


class TecnologiaPost(Post):

    objects = TecPostManager()

    class Meta:
        proxy = True


class UserInfo(User):
    bio = models.TextField()


class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2) 

    class Meta:
        abstract = True


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Destinatatio(Contato, Endereco, Auditoria):
    cpf = models.CharField(max_length=15)


class Remetente(Endereco, Contato, Auditoria):
    cnpj = models.CharField(max_length=15)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    age = models.DateField(null=True, blank=True)
    twitter = models.CharField(null=True, blank=True, max_length=60)

    def __str__(self):
        return self.user.username


class Automovel(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    slug = models.CharField(max_length=100)
