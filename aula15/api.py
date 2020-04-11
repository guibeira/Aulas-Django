from rest_framework import serializers
from django.db import transaction
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import MyCustomSerializer, ClientSerializer

from django.contrib.auth.models import User, Permission


class PersmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"



class UserSeriaizer(serializers.ModelSerializer):
    user_permissions = PersmissionSerializer(required=True)

    class Meta:
        model = User
        fields = ["username", "user_permissions"] 

    def create(self, data, *args, **kwargs):
        with transaction.atomic():
            user = User.objects.create(username=data.pop('username'))
            permisison, _ = Permission.objects.get_or_create(**data['user_permissions'])
            user.user_permissions.add(permisison)
        return self.validated_data


class SerializerTestView(CreateAPIView):
    serializer_class = UserSeriaizer

    def get(self, request, *args, **kwargs):
        return Response({'message': 'teje bem vinu!'})
