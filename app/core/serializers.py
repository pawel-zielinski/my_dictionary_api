from rest_framework.serializers import ModelSerializer, Serializer

from core.models import User, Event


class HomeSerializer(Serializer):
    class Meta:
        model = Event
        fields = (
            'name',
            'organizer',
            'tags',
            'date',
        )


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'name',
            'organizer',
            'guests',
            'tags',
            'attachment',
            'date',
            'notes',
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'profile',
        )
