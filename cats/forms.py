from django import forms
from .models import Cats


class CatsForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name_cat', 'ascii_cat', 'desc_cat']

        labels = {
            'name_cat': 'Nombre',
            'ascii_cat': 'Gato',
            'desc_cat': 'Descripcion',
        }

        widgets = {
            'name_cat': forms.TextInput(attrs={'class': 'form-control'}),
            'ascii_cat': forms.Textarea(attrs={'class': 'form-control'}),
            'desc_cat': forms.Textarea(attrs={'class': 'form-control'}),
        }