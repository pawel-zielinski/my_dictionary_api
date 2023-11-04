from rest_framework import permissions

from core.models import User


class EventPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return User.objects.get(username=request.user.username).profile == 'organizer'
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'destroy']:
            return obj.organizer == request.user
        return True


class DocumentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'destroy']:
            return obj.author == request.user


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'destroy']:
            return obj == request.user
        return True
