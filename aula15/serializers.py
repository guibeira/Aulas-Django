from django.contrib.auth.models import Permission, User
from django.db import transaction
from rest_framework import serializers


class MyCustomSerializer(serializers.Serializer):
    choices = (
        ("M", "masculino"),
        ("F", "feminino"),
    )

    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    text = serializers.CharField(max_length=500)
    sexo = serializers.ChoiceField(choices)

    def create(self, *args, **kwags):
        return self.validated_data

    def validate_email(self, value):
        if "guilherme" in value.lower():
            raise serializers.ValidationError("Guilherme ta proibido!")
        return value

    def validate_text(self, value):
        if "babanao" in value.lower():
            raise serializers.ValidationError("Seu boca suja!")
        return value


class AddressSerializer(serializers.Serializer):
    choices = (
        ("residencial", "residencia"),
        ("comercial", "comercial"),
    )
    street = serializers.CharField(max_length=30)
    number = serializers.IntegerField()
    neighborhood = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    cowntry = serializers.CharField(max_length=2)
    address_type = serializers.ChoiceField(choices)


class ClientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30)
    address = AddressSerializer(required=True, many=True)

    def create(self, *args, **kwags):
        return self.validated_data


class PersmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
