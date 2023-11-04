from django.shortcuts import render
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, \
    ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from core.models import Event, User, Document
from core.permissions import EventPermission, UserPermission, DocumentPermission
from core.serializers import HomeSerializer, EventSerializer, UserSerializer, DocumentSerializer


class HomeViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (IsAuthenticated, EventPermission)


class EventViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, EventPermission,)


class UserViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, UserPermission,)


class DocumentViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated, DocumentPermission,)
