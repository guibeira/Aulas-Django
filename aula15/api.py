from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClientSerializer, UserSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated



class OnlySelfUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True
        return user == obj.created_by


class SerializerTestView(CreateAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response({'message': 'teje bem vinu!'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, OnlySelfUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    model = User
