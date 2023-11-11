from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin, \
    ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.forms import EventForm
from core.models import Event, User, Document
from core.permissions import EventPermission, UserPermission, DocumentPermission
from core.serializers import HomeSerializer, EventSerializer, UserSerializer, DocumentSerializer


class HomeViewSet(GenericViewSet, ListModelMixin):
    template_name = 'home.html'
    renderer_classes = (TemplateHTMLRenderer,)
    queryset = Event.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (IsAuthenticated,)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, EventPermission,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'features/event_list.html'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data}, template_name='features/event_detail.html')

    @action(detail=True, methods=['get', 'post'])
    def events(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Event created successfully')

        queryset = self.get_queryset()
        return Response({'form': form, 'events': queryset})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)


class UserViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, UserPermission,)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated, DocumentPermission,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
