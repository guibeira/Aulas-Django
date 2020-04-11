from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Loja
from .serializer import LojaSerializer

# Create your views here.


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=40)
    email = serializers.EmailField()


class MyGenericCreateAndList(APIView):
    model = None
    queryset = None
    serializer_class = None

    def _get_model(self):
        if self.model is None:
            raise ("Cade o model!!!!")
        return self.model

    def _get_queryset(self):
        if self.queryset is None:
            raise ("Cade o queryset!!!!")
        return self.queryset.all()

    def _get_serializer_class(self):
        if self.serializer_class is None:
            raise ("Cade o serializer_class!!!!")
        return self.serializer_class

    def get(self, request):
        queryset = self._get_queryset()
        serializer_class = self._get_serializer_class()
        user_results = []
        for data in queryset:
            serialized_user = serializer_class(data=model_to_dict(data))
            serialized_user.is_valid()
            user_results.append(serialized_user.data)
        return Response({"results": user_results})

    def post(self, request):
        serializer_class = self._get_serializer_class()
        serialized_user = serializer_class(data=request.data)
        model = self._get_model()
        if serialized_user.is_valid():
            validated_model = model(**serialized_user.validated_data)
            validated_model.save()
            return Response({"data": serialized_user.data}, status=201)
        return Response({"erros": serialized_user.errors})


class UserViewset(MyGenericCreateAndList):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LojaViewSet(
    ListAPIView, CreateAPIView,
):
    model = Loja
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
