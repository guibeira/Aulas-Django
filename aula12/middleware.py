from django.conf import settings
from django.http import HttpResponseRedirect


class MyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print(f"Acessando a url {request.path}")
        response = self.get_response(request)
       
        return response


class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != settings.LOGIN_URL:
            return HttpResponseRedirect(settings.LOGIN_URL)

        response = self.get_response(request)
       
        return response
