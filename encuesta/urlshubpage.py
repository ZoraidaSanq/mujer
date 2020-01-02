from django.urls import path
from .views import (index,log,encuesta,logoutview,preguntaresul,mujer2,resultado)
from django.contrib.auth import authenticate, login, logout



app_name='hubpage'
urlpatterns = [ 
    path('', index,name='pa1'),
    path('resultado/<int:pk>',resultado,name='resultado'),
    path('enc/<str:nombre>/<int:pk>', encuesta,name='encuesta'),
    path('enc/<str:nombre>/<int:pk>/<int:pkqr>',preguntaresul,name='usuario_app'),
    

   # path('encuesta/', mujer,name='pa2'),
    #path('encuesta/<str:questionario>/<int:pk>', mujer2,name='pa3'),
    path('login/', log, name='pa4'),
    path('logout', logoutview, name="logout"),
    path('intranet/', mujer2,name='pa3'),
   


    
  
 
]
