import os
import uuid
from datetime import date

from django.db import models
from django.contrib.auth.models import User as DjangoUser


def document_file_patch(instance, filename):
    """Generate file path for new documents."""
    dt = date.today()
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join(f'document_files/{dt.year}/{dt.month}/{dt.day}/', filename)


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


class Document(models.Model):
    title = models.CharField(max_length=256)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    attachment = models.FileField(upload_to=document_file_patch)
    summary = models.CharField(max_length=1024)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'[{self.course.name}] ({self.date_added}) -- "{self.title}"'


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
