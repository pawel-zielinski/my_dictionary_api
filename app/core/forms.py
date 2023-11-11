from django import forms
from core.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'guests', 'tags', 'date', 'attachment', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }
