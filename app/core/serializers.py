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
    organizer = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'organizer',
            'guests',
            'tags',
            'attachment',
            'date',
            'notes',
        )

    @staticmethod
    def get_organizer(obj):
        return obj.organizer

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
    author = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = (
            'id',
            'title',
            'author',
            'course',
            'attachment',
            'summary',
            'date_added',
        )

    @staticmethod
    def get_author(obj):
        return f'{obj.author.first_name} {obj.author.last_name}'

    @staticmethod
    def get_course(obj):
        return obj.course.name

    def create(self, validated_data):
        author = User.objects.get(username=self.context['request'].user.username)
        validated_data.update({'author': author})
        return super().create(validated_data)
