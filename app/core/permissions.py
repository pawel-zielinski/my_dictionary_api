from rest_framework import permissions


class EventPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.profile.name == 'organizer'
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'destroy']:
            return obj.organizer == request.user
        return True


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'destroy']:
            return obj == request.user
        return True
