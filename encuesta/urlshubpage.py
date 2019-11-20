from django.urls import path
from .views import (index,mujer,log,mujer2,repor,encuesta)

app_name='hubpage'
urlpatterns = [ 
    path('', index,name='pa1'),
    path('enc/<str:nombre>/<int:pk>', encuesta,name='encuesta'),






    path('encuesta/', mujer,name='pa2'),
    #path('encuesta/<str:questionario>/<int:pk>', mujer2,name='pa3'),
    path('login/', log, name='pa4'),
    path('intranet/', mujer2,name='pa3'),
    path('rep/', repor,name='pa5'),

    #path('perfil/<str:nombre>', primera_vista),
]
