from django.contrib import admin

from core.models import User, Event, Profile, Tag, Course, Document

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Document)
admin.site.register(Course)
