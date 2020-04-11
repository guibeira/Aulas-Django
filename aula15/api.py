from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import MyCustomSerializer, ClientSerializer, UserSeriaizer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class SerializerTestView(CreateAPIView):
    serializer_class = UserSeriaizer

    def get(self, request, *args, **kwargs):
        return Response({'message': 'teje bem vinu!'})
