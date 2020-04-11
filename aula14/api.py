from rest_framework import viewsets

from .models import Carros
from .serializer import CarrosSerializer


class CarrosViewSet(viewsets.ModelViewSet):
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer
