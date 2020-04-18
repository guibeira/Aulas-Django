from rest_framework.viewsets import ModelViewSet

from .models import Hero
from .serializers import HeroSerializer


class HeroViewSet(ModelViewSet):
    model = Hero
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
