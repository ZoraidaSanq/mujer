from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db.transaction import atomic




def index(request):
    _encuesta = Encuesta.objects.filter(isuso=True,estado=True)
    context = {'encuesta': _encuesta}
    return render(request, 'hubpage/index.html', context)


def encuesta(request, nombre=None, pk=None):
    context = {
        'formmujer': MujerForm
        #'formpregunta': PreguntaForm
    }
    if request.method == 'POST':
        formmujer = MujerForm(request.POST)
        context ={
            'formmujer': formmujer
            }
        if formmujer.is_valid():
           with atomic ():
                omujer = formmujer.save(commit=False)
                omujer.save()
                oencuesta = Encuesta.objects.first()
                oencuestaMujer = EncuestaMujer(
                    nombre=oencuesta.nombre,
                    num_pre_asig = oencuesta.num_pre_asig,
                    num_pre_resuelta=0,
                    encuesta=oencuesta,
                    mujer=omujer
                )
                oencuestaMujer.save()
                pkqr=oencuestaMujer.id
                nombreencuesta=oencuesta.nombre.replace ('','-')
                pk=oencuesta.id 
                return redirect('hubpage:usuario_app',nombreencuesta,pk,pkqr)

    return render(request, 'encuesta/encuesta.html', context)

from django.forms import formset_factory

def preguntaresul(request,nombre=None,pk=None,pkqr=None):
    _encuesta = Encuesta.objects.filter(estado=True,isuso=True,id=pk).first()
    a = Pregunta.objects.first()
    falsoq = [{'encuesta_id':pk,'pregunta':i.pregunta,'pregunta_id': i.id}
            for i in Pregunta.objects.filter(encuesta_id=pk,estado=True,isuso=True) ]
    #print(falsoq)
    PreguntaFormFormSet = formset_factory(PreguntaForm2,max_num=falsoq.__len__())

    context ={
        "encuesta" :_encuesta,
        "formset" :PreguntaFormFormSet(initial=falsoq)
    }
    return render(request, 'encuesta/listarenc.html',context)
          
        



"""
 "form" :PreguntaForm2(encuesta_id=a.encuesta_id,
                    pregunta=a.pregunta,
                    id=a.id)
"""


def log(request):
    if request.method == 'POST':
        #return redirect('/adminpage/ta_base')
    #elif request.method == 'POST':
        variable1 = str(request.POST.get('campo1'))
        variable2 = str(request.POST.get('campo2'))
        user = authenticate(request, username=variable1, password=variable2)
        if user is not None:
            login(request, user)
            return  redirect('/intranet')
    return render (request, 'login/logadmin.html')

def logoutview(request):
    logout(request)

    return redirect('login/')


def mujer2(request):
    context = {}
    return render(request, 'adminpage/ta_base.html', context)


def repor(request):
    context = {}
    return render(request, 'reportes/listarencuesta.html', context)




def encuesta2(request):
    context = {}
    return render(request, 'encuesta/listarenc.html', context)

def preguntaresp(request):
    context = {}
    return render(request, 'encuesta/listarenc.html', context)

