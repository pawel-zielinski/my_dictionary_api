from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from core.models import User, Event, Document


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
            'guests',
            'tags',
            'attachment',
            'date',
            'notes',
        )

    def create(self, validated_data):
        organizer = User.objects.get(username=self.context['request'].user.username)
        validated_data.update({'organizer': organizer})
        return super().create(validated_data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'profile',
        )


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'title',
            'course',
            'attachment',
            'summary',
            'date_added',
        )

    def create(self, validated_data):
        author = User.objects.get(username=self.context['request'].user.username)
        validated_data.update({'author': author})
        return super().create(validated_data)
