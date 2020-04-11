from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    twitter = models.URLField()
    data_nascimento = models.DateField(null=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name="posts")

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    autor = models.CharField(max_length=30)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor} no post {self.post}"


class Carrinho(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = self.produto_set.all().aggregate(models.Sum("preco"))
        return total["preco__sum"]


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.FloatField()
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
