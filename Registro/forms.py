from django import forms
from .models import Cats
from django.contrib import messages


class CatsForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name_cat', 'ascii_cat', 'desc_cat', 'imagen_cat']

        labels = {
            'name_cat': 'Nombre',
            'ascii_cat': 'Gato',
            'desc_cat': 'Descripcion',
            'imagen_cat': 'Imagen',
        }
        widgets = {
            
            'name_cat': forms.TextInput(attrs={'class': 'form-control'}),
            'ascii_cat': forms.Textarea(attrs={'class': 'form-control'}),
            'desc_cat': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_cat': forms.FileInput(attrs={'class': 'form-control'}),
        }



# PorSiAcaso


class CatsFormValidate(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['id', 'name_cat', 'ascii_cat', 'desc_cat', 'imagen_cat']

        labels = {
            'id': 'id',
            'name_cat': 'Nombre',
            'ascii_cat': 'Gato',
            'desc_cat': 'Descripcion',
            'imagen_cat': 'Imagen',
        }

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_cat': forms.TextInput(attrs={'class': 'form-control'}),
            'ascii_cat': forms.Textarea(attrs={'class': 'form-control'}),
            'desc_cat': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_cat': forms.FileInput(attrs={'class': 'form-control'}),
        }
