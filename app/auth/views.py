from auth.serializers import RegisterSerializer
from auth.serializers import TokenObtainerSerializer
from core.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtainTokenViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainerSerializer


class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
