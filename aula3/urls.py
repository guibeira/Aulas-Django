from django.urls import path
from .views import index, setacookie, redireciona

app_name = "aula3"

urlpatterns = [
    path('', index),
    path('cookie', setacookie),
    path('uol', redireciona)
] 
