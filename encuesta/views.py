from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'nombre': ' soy alguien'}
    return render(request, 'hubpage/algo.html', context)


def mujer(request):
    context = {}
    return render(request, 'hubpage/pag1.html', context)


# def mujer2(request,questionario=None,pk=None):
 #   context={}
  #  return render(request, 'adminpage/ta_base.html', context)

def log(request):
    context={}
    return render(request, 'login/logadmin.html', context)


def mujer2(request):
    context={}
    return render(request, 'adminpage/ta_base.html', context)


def repor(request):
    context={}
    return render(request, 'reportes/listarencuesta.html', context)


def encuesta(request):
    context={}
    if request.method == 'POST':
        print(request.POST.get('ocupacion'))
    return render(request, 'encuesta/tj.html', context)

def encuesta2(request):
    context={}
    return render(request, 'encuesta/questionario.html', context)