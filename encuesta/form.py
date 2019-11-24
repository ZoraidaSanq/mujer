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
    pregunta_id = forms.IntegerField ()
    pregunta = forms.CharField (max_length=100)
    likert = forms.IntegerField(widget=forms.Select)
    def __init__(self, *args, **kwargs):
        print(kwargs)
        encuestaid = kwargs.pop('encuesta_id')
        pregunta = kwargs.pop('pregunta')
        pregunta_id = kwargs.pop('id')

        super(PreguntaForm2, self).__init__(*args, **kwargs)
        self.fields['likert']=forms.ModelChoiceField(queryset=Likert.objects.filter(encuesta_id=int(encuestaid)))
        self.fields['pregunta'].initial=pregunta
        self.fields['pregunta_id'].initial=int(pregunta_id)



    

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

