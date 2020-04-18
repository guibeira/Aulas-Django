"""cursodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from aula4.views import index
from aula6.views import editar_contato
from aula6.views import index as index6
from aula7.views import index as index7
from aula7.views import logout_view, permission_view, restrita
from aula9.views import index9
from aula10.views import mostra_arquivo_estatico
from aula11.views import PostDetailView, aula11
from aula13.views import OlistRedirect, aula13, aula13_com_model_form, aula13_session
from aula14.api import CarrosViewSet
from aula14.views import LojaViewSet
from aula15.api import SerializerTestView, UserViewSet
from aula15.authentication import GetTokenAndExtraInfo

routes = routers.DefaultRouter()
routes.register(r"carros", CarrosViewSet)
routes.register(r"users", UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("aula3.urls")),
    path("estatico", mostra_arquivo_estatico, name="aula10"),
    path("aula4/", index),
    path("aula6/", index6),
    path("aula6/<int:id>", editar_contato),
    path("entrar/", index7, name="login"),
    path("aula7/restrita/", restrita),
    path("aula7/view-carrinho/", permission_view),
    path("aula7/sair/", logout_view, name="logout"),
    path("aula9/", index9, name="aula9"),
    path("aula11/", aula11, name="aula11"),
    path("aula11/<str:slug>", PostDetailView.as_view()),
    path("aula13/", include("aula13.urls")),
    path("aula14-a/", LojaViewSet.as_view(), name="aula14-a"),
    path("aula15/", SerializerTestView.as_view(), name="aula15"),
    # api
    path("v1/", include(routes.urls)),
    path("v1/cade-meu-token", GetTokenAndExtraInfo.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

