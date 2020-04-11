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


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"
