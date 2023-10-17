from django.shortcuts import render
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.models import Event, User
from core.serializers import HomeSerializer, EventSerializer, UserSerializer


class HomeViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    queryset = Event.objects.all()
    serializer_class = HomeSerializer


class EventViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
