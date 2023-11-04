from django.contrib.auth import login, logout
from django.shortcuts import redirect
from rest_framework import views, permissions, status, generics
from rest_framework.response import Response

from auth.serializers import LoginSerializer, RegisterSerializer
from core.models import User


class LoginView(views.APIView):
    """Thesis Degree API login APIView."""
    permission_classes = (permissions.AllowAny,)

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


class LogoutView(views.APIView):
    """Thesis Degree API logout APIView."""
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """Post logout signal to log authenticated user out."""
        logout(request)
        return redirect('/auth/login/')


class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
