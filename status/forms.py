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
                attrs = {
                    'class' : 'container-fluid form-control',
                    'id' : 'form-title',
                     }
            ),
            'content' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control', 
                    'id' : 'form-content',
                    }
            ),
            'image' : forms.FileInput(
                attrs = {
                    'id' : 'form-image'
                }
            )
        }