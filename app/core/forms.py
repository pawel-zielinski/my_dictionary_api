from django import forms
from core.models import Event, User, Document


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


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'course', 'attachment', 'summary')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, author=None, commit=True, **kwargs):
        instance = super(DocumentForm, self).save(commit=False)
        instance.author = User.objects.get(id=author.id) if author else self.instance.author
        if commit:
            instance.save()
        return instance
