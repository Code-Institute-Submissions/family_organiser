from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'information', 'header_image', 'event_date', 'start_time', 'end_time', 'location')
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'placeholder': 'Family Dinner',
                    }
            ),
            'information' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'placeholder': 'Family dinner at the "Dinner Palace"...',
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
            ),
            'start_time' : forms.DateTimeInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'type' : 'time'
                    }
            ),
            'end_time' : forms.DateTimeInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'type' : 'time'
                    }
            ),
            'location' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'type' : 'text',
                    'placeholder': '3 Walk Street, Dinner Palace',
                    }
            )
        }
        