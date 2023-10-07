from django.shortcuts import render
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from core.models import Event, User
from core.serializers import HomeSerializer, EventSerializer, UserSerializer


class HomeViewSet(CreateModelMixin, RetrieveModelMixin):
    class Meta:
        queryset = Event.objects.all()
        serializer_class = HomeSerializer


class EventViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    class Meta:
        queryset = Event.objects.all()
        serializer_class = EventSerializer


class UserViewSet(RetrieveModelMixin, UpdateModelMixin):
    class Meta:
        queryset = User.objects.all()
        serializer_class = UserSerializer
