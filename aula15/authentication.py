import time
from random import randint
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class GetTokenAndExtraInfo(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        payload = {"token": token.key, "user_id": user.pk, "email": user.email}
        return Response(payload)

    def get(self, request):
        cached_result = cache.get("result")
        if cached_result:
            result_calc = cached_result
        else:
            time.sleep(10)
            result_calc = randint(0, 100)
            cache.add("result", result_calc, timeout=15)
        return Response({"amount": result_calc})


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
