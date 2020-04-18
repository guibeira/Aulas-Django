from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(5))
    def get(self, request):
        users = User.objects.all()
        user = users[0]
        return Response({"email": user.email})


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
