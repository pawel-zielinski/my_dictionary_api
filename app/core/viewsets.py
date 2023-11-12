from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import UpdateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.forms import EventForm, DocumentForm
from core.models import Event, User, Document
from core.permissions import EventPermission, UserPermission, DocumentPermission
from core.serializers import HomeSerializer, EventSerializer, UserSerializer, DocumentSerializer


class HomeViewSet(GenericViewSet, ListModelMixin):
    template_name = 'home.html'
    renderer_classes = (TemplateHTMLRenderer,)
    queryset = Event.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (IsAuthenticated,)


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'features/event_update.html'

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        self.success_url = f'/event/{pk}'
        return Event.objects.get(pk=pk)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, EventPermission,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'features/event_list.html'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        is_guest = User.objects.get(username=request.user.username) in instance.guests.all()
        return Response({'data': serializer.data, 'is_guest': is_guest}, template_name='features/event_detail.html')

    @action(detail=True, methods=['get', 'post'])
    def events(self, request, *args, **kwargs):
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Event created successfully')

        queryset = self.get_queryset()
        is_organizer = User.objects.get(username=request.user.username).profile.name == 'organizer'
        return Response({'form': form, 'events': queryset, 'is_organizer': is_organizer})

    @action(detail=True, methods=['post'])
    def signin(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs['pk'])
        user = User.objects.get(username=request.user.username)
        if user in event.guests.all():
            event.guests.remove(user)
            messages.info(request, 'You have been removed from the event')
        else:
            event.guests.add(user)
            messages.info(request, 'You have been added to the event')
        return redirect(f'/event/{kwargs["pk"]}')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        messages.info(request, 'Event deleted successfully')
        return HttpResponseRedirect(redirect_to='/event/')


class UserViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, UserPermission,)


class DocumentUpdateView(UpdateView):
    model = Event
    form_class = DocumentForm
    template_name = 'features/docs_update.html'

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        self.success_url = f'/docs/{pk}'
        return Document.objects.get(pk=pk)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-date_added')
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated, DocumentPermission,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'features/docs_list.html'

    def get_queryset(self):
        queryset = Document.objects.all()
        course_name_contains = self.request.query_params.get('course_name_contains', None)
        title_contains = self.request.query_params.get('title_contains', None)
        if course_name_contains:
            queryset = queryset.filter(course__name__icontains=course_name_contains)
        elif title_contains:
            queryset = queryset.filter(title__icontains=title_contains)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        is_author = instance.author == User.objects.get(username=request.user.username)
        return Response({'data': serializer.data, 'is_author': is_author}, template_name='features/docs_detail.html')

    @action(detail=True, methods=['get', 'post'])
    def docs(self, request, *args, **kwargs):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(author=request.user)
            messages.info(request, 'Document created successfully')

        queryset = self.get_queryset()
        return Response({'form': form, 'docs': queryset})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        messages.info(request, 'Document deleted successfully')
        return HttpResponseRedirect(redirect_to='/docs/')
