from django.urls import path
from rest_framework.routers import DefaultRouter
from core.viewsets import HomeViewSet, EventViewSet, UserViewSet, DocumentViewSet, EventUpdateView, DocumentUpdateView, \
    UserUpdateView

router = DefaultRouter()
router.register('home', HomeViewSet, basename='homepage')
router.register('user', UserViewSet, basename='userpage')
router.register('docs', DocumentViewSet, basename='document')

urlpatterns = [
    path('event/', EventViewSet.as_view({'get': 'events', 'post': 'events'}), name='eventpage'),
    path('event/<int:pk>/', EventViewSet.as_view({'get': 'retrieve'}), name='eventpage-detail'),
    path('event/<int:pk>/edit', EventUpdateView.as_view(), name='eventpage-update'),
    path('event/<int:pk>/delete', EventViewSet.as_view({'post': 'destroy'}), name='eventpage-delete'),
    path('event/<int:pk>/signin', EventViewSet.as_view({'post': 'signin'}), name='eventpage-signin'),
    path('docs/', DocumentViewSet.as_view({'get': 'docs', 'post': 'docs'}), name='docspage'),
    path('docs/<int:pk>/', DocumentViewSet.as_view({'get': 'retrieve'}), name='docspage-detail'),
    path('docs/<int:pk>/edit', DocumentUpdateView.as_view(), name='docspage-update'),
    path('docs/<int:pk>/delete', DocumentViewSet.as_view({'post': 'destroy'}), name='docspage-delete'),
    path('user/<int:pk>/edit', UserUpdateView.as_view(), name='userpage-update'),
]
urlpatterns += router.urls
