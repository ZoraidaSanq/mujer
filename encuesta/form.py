from django import forms
from .models import Mujer,Pregunta,Encuesta,EncuestaMujer,Preguntaresultado,Likert


class MujerForm(forms.ModelForm):
    class Meta:
        model = Mujer
        fields = '__all__'
        widgets = {
            'ocupacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),
            'estadocivil': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ingresa una descripcion'}),
            'nivel_educacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa una descripcion'}),
            'hijos': forms.NumberInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['pregunta','orden']
        widgets = {
            'pregunta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class PreguntaForm2(forms.Form):
    pregunta_id = forms.IntegerField(required=False)
    pregunta = forms.CharField (max_length=100,required=False)
    likert = forms.IntegerField(widget=forms.Select(attrs={'required':'required'}),required=True)
    def __init__(self, *args, **kwargs):
        super(PreguntaForm2, self).__init__(*args, **kwargs)
        if kwargs.get('initial'):
            encuesta_id = kwargs.get('initial').get('encuesta_id')
            self.fields['likert']=forms.ModelChoiceField(queryset=Likert.objects.filter(encuesta_id=encuesta_id))
            self.fields['likert'].widget.attrs['class'] = 'form-control'
            self.fields['likert'].widget.attrs['required'] = 'required'


  

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),
            #'estado': forms.BooleanField(attrs={'class': 'form-control', 'placeholder': ''}),

        }

class EncuestaMujerForm(forms.ModelForm):
    class Meta:
        model = EncuestaMujer
        fields = ['nombre','estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa su ocupacion'}),

        }


class PreguntaResultadoForm(forms.ModelForm):
    class Meta:
        model = Preguntaresultado
        fields = '__all__'
        widgets = {
            'pregunta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),

        }

