from django.urls import path
from rest_framework.routers import DefaultRouter
from core.viewsets import HomeViewSet, EventViewSet, UserViewSet, DocumentViewSet, EventUpdateView

router = DefaultRouter()
router.register('home', HomeViewSet, basename='homepage')
router.register('user', UserViewSet, basename='userpage')
router.register('docs', DocumentViewSet, basename='document')

urlpatterns = [
    path('event/', EventViewSet.as_view({'get': 'events', 'post': 'events'}), name='eventpage'),
    path('event/<int:pk>/', EventViewSet.as_view({'get': 'retrieve'}), name='eventpage-detail'),
    path('event/<int:pk>/edit', EventUpdateView.as_view(),
         name='eventpage-update'),
]
urlpatterns += router.urls
