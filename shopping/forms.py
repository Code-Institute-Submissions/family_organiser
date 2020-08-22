from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item', 'quantity')
        widgets = {
            'item' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'id': 'form-item'
                     }
            ),
            'quantity' : forms.NumberInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'id': 'form-quantity'
                     }
            )
        }