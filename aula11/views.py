from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Post


def aula11(request):
    posts = Post.objects.select_related("categoria").all()
    return render(request, "aula11/index.html", {"posts": posts})


class PostDetailView(DetailView):
    model = Post
    template_name = "aula11/detalhe.html"

    def get_slug_field(self):
        return "title"
