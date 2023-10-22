from auth.views import ObtainTokenViewSet
from auth.views import RegisterViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', ObtainTokenViewSet.as_view(), name='token_obtainer'),
    path('login/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', RegisterViewSet.as_view(), name='auth_register')
]
