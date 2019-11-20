from django import forms
from .models import Mujer


class MujerForm(forms.ModelForm):
    class Meta:
        model = Mujer
        fields = '__all__'
        widgets = {
            'ocupacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),
            'estadocivil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa una descripcion'}),
            'nivel_educacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa una descripcion'}),
            'hijos': forms.NumberInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),

        }
