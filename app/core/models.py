from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    profile = models.ForeignKey('Profile', on_delete=models.RESTRICT, related_name='profile')

    def __str__(self):
        return f'({self.profile}) {self.username} -- {self.email}'


class Event(models.Model):
    name = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer')
    guests = models.ManyToManyField(User, related_name='guests')
    tags = models.ManyToManyField('Tag', related_name='tags')
    date = models.DateTimeField()
    attachment = models.FileField()
    notes = models.CharField(max_length=250)

    def __str__(self):
        return f'[{", ".join(tag.name for tag in self.tags.all())}] ({self.date.strftime("%d-%m-%Y")}) -- "{self.name}"'


class Profile(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
