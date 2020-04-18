from django.urls import path

from . import views

app_name = "aula13"

urlpatterns = [
    path("upload", views.aula13, name="aula13"),
    path("session", views.aula13_session, name="aula13-session"),
    path("model", views.aula13_com_model_form, name="aula13-model"),
    path("olist-redirect", views.OlistRedirect.as_view()),
]
