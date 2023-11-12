from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import views, permissions, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from auth.serializers import LoginSerializer, RegisterSerializer
from core.models import User


class LoginView(views.APIView):
    """Thesis Degree API login APIView."""
    permission_classes = (~permissions.IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'auth/login.html'

    def get(self, request, format=None):
        """Get login page."""
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        """Post login data to authenticate."""
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        if user.is_authenticated:
            response = redirect('/home/')
        else:
            response = Response(None, status=status.HTTP_401_UNAUTHORIZED)
        return response


@login_required
def log_out(request):
    logout(request)
    messages.warning(request, 'Logged Out')
    return HttpResponseRedirect(reverse('login'))


class RegisterViewSet(views.APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'auth/register.html'
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def get(self, request, format=None):
        """Get login page."""
        serializer = RegisterSerializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/auth/login/')
        return Response({'serializer': serializer})
