from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    profile = models.ForeignKey('Profile', on_delete=models.RESTRICT, related_name='profile')


class Event(models.Model):
    name = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='organizer')
    guests = models.ManyToManyField(User, related_name='guests')
    tags = models.ManyToManyField('Tag', related_name='tags')
    date = models.DateTimeField()
    attachment = models.FileField()
    notes = models.CharField(max_length=250)


class Profile(models.Model):
    name = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)
