from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'information', 'header_image', 'event_date')
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control'
                    }
            ),
            'information' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control'
                    }
            ),
             'header_image' : forms.FileInput(
                attrs = {
                    'class' : 'container-fluid form-control'
                    }
            ),
             'event_date' : forms.DateTimeInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'type' : 'date'
                    }
            )
        }
        