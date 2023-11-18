from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in [reverse('login'), reverse('auth_register')]:
            return HttpResponseRedirect(reverse('login'))
        response = self.get_response(request)
        return response
