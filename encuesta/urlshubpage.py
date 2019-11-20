from django.urls import path
from .views import (index,mujer,log,mujer2,repor,encuesta,encuesta2)

app_name='hubpage'
urlpatterns = [ 
    path('', index,name='pa1'),
    path('encuesta/', mujer,name='pa2'),
    #path('encuesta/<str:questionario>/<int:pk>', mujer2,name='pa3'),
    path('login/', log, name='pa4'),
    path('intranet/', mujer2,name='pa3'),
    path('rep/', repor,name='pa5'),
    path('test1mujer/', encuesta,name='pa6'),
    path('test2mujer/', encuesta2,name='pa7'),

    #path('perfil/<str:nombre>', primera_vista),
]
