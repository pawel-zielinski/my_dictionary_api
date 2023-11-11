from django.urls import path

from auth.views import RegisterViewSet, LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterViewSet.as_view(), name='auth_register')
]
