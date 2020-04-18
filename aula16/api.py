from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import (AnonRateThrottle, ScopedRateThrottle,
                                       UserRateThrottle, BaseThrottle)
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Hero
from .serializers import HeroSerializer


class CustomFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(name="Batman")


class MyCustomThrottle(BaseThrottle):

    def allow_request(self, request, view):
        # regra de x request por x tempo
        return True


class ModelHoreScopeViewSet(ModelViewSet):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "heros"


class HeroViewSet(ModelViewSet):
    throttle_classes = [MyCustomThrottle]
    model = Hero
    serializer_class = HeroSerializer
    filter_backends = [CustomFilter, OrderingFilter, SearchFilter]
    queryset = Hero.objects.all()
    filterset_fields = ["name", "super_power"]    
    search_fields = ["name", "super_power", "city"]
    ordering_fields = ["name", "super_power", "city"]

    @action(methods=["get"], detail=False, url_path="poderes")
    def show_list_hero_powers(self, request):
        heros = self.get_queryset()
        results = [{hero.name: hero.super_power} for hero in heros]
        return Response({"results": results})
    
    @action(methods=["get"], detail=True, url_path="poder")
    def heropower(self, request, pk=None):
        hero = self.get_object()
        return Response({"hero": hero.super_power})
