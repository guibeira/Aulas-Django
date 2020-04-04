from django.db import models


class Loja(models.Model):
    cidade = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}"


class Carros(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, null=True)
    ano = models.DateField()

    def __str__(self):
        return f"{self.marca} {self.modelo}"
