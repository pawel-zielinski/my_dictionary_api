from rest_framework.routers import DefaultRouter
from core.viewsets import HomeViewSet, EventViewSet, UserViewSet


router = DefaultRouter()
router.register('home', HomeViewSet, basename='homepage')
router.register('event', EventViewSet, basename='eventpage')
router.register('user', UserViewSet, basename='userpage')

urlpatterns = []
urlpatterns += router.urls
