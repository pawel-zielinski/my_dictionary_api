from django.urls import path

from auth.views import RegisterViewSet, LoginView, log_out

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', RegisterViewSet.as_view(), name='auth_register')
]
