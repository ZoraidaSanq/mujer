from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={'nombre':' soy alguien'}
    return render(request, 'encuesta/pag1.html', context)

def mujer(request):
    context={'nombre':' soy alguien'}
    return render(request, 'ta_aside.html', context)


