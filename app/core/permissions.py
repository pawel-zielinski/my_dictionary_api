from rest_framework import permissions


class EventPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        if view.action in ['update', 'destroy']:
            return obj.organizer == request.user
        return False
