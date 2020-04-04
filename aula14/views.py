from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your views here.


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=40)
    email = serializers.EmailField()


@api_view(['GET', 'POST'])
def aula14(request):
    if request.method == 'POST':
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            username = serialized_user.validated_data["username"]
            email = serialized_user.validated_data["email"]
            user = User(username=username, email=email)
            user.save()
            return Response({'user': serialized_user.data}, status=201)
        return Response({'erros': serialized_user.errors})
    users = User.objects.all()
    user_results = []
    for user in users:
        data = {"username": user.username, "email": user.email}
        serialized_user = UserSerializer(data=data)
        serialized_user.is_valid()
        user_results.append(serialized_user.data)
    return Response({"users": user_results}) 