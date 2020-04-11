from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .authentication import BearerTokenAuthentication
from .serializers import UserSerializer


class SerializerTestView(CreateAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "teje bem vinu!"})


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    model = User
