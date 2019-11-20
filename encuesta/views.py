from django.shortcuts import render
from django.http import HttpResponse
from .form import MujerForm
from .models import (Encuesta)


def index(request):
    _encuesta = Encuesta.objects.filter(isuso=True,estado=True)
    context = {'encuesta': _encuesta}
    return render(request, 'hubpage/index.html', context)


def encuesta(request, nombre=None, pk=None):
    context = {
        'formmujer': MujerForm
    }
    if request.method == 'POST':
        formmujer = MujerForm(request.POST)
        if formmujer.is_valid():
            formmujer.save()
        context = {
            'formmujer': formmujer
        }

    return render(request, 'encuesta/encuesta.html', context)


def mujer(request):
    context = {}
    return render(request, 'hubpage/pag1.html', context)


# def mujer2(request,questionario=None,pk=None):
 #   context={}
  #  return render(request, 'adminpage/ta_base.html', context)

def log(request):
    context = {}
    return render(request, 'login/logadmin.html', context)


def mujer2(request):
    context = {}
    return render(request, 'adminpage/ta_base.html', context)


def repor(request):
    context = {}
    return render(request, 'reportes/listarencuesta.html', context)




def encuesta2(request):
    context = {}
    return render(request, 'encuesta/listarenc.html', context)
