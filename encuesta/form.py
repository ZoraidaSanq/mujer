from django import forms
from .models import Mujer,Pregunta,Encuesta


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


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['pregunta','likert','orden']
        widgets = {
            'pregunta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),
            'likert': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ingresa una descripcion'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),

        }

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre','estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),
            #'estado': forms.BooleanField(attrs={'class': 'form-control', 'placeholder': ''}),

        }