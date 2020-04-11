from rest_framework.generics import CreateAPIView
from .serializers import MyCustomSerializer

class SerializerTestView(CreateAPIView):
    serializer_class = MyCustomSerializer
