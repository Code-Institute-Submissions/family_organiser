from django import forms
from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['title', 'content', 'image']
        labels = {
            'content': 'post'
        }
        widgets = {
            'title' : forms.TextInput(
                attrs = {'class' : 'container-fluid form-control', }
            ),
            'content' : forms.TextInput(
                attrs = {'class' : 'container-fluid form-control', }
            ),
        }