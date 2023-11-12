from django import forms
from core.models import Event, User


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'organizer', 'guests', 'tags', 'date', 'attachment', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'organizer': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }
