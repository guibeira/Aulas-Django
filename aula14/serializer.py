from rest_framework import serializers

from .models import Carros, Loja


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ["cidade", "nome"]


class CarrosSerializer(serializers.ModelSerializer):
    loja = LojaSerializer()
    class Meta:
        model = Carros
        fields = ["modelo", "marca", "loja", "ano"]
