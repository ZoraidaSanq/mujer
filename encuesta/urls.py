from django.urls import path
from .views import (index,mujer)

app_name='encuesta'
urlpatterns = [
    path('p1/', index,name='pa1'),
    path('modulos/', mujer,name='pa2'),
    path('pregunta/', mujer,name='pa3'),

    #path('perfil/<str:nombre>', primera_vista),
]
