from django.urls import path
from .views import (index)

app_name='encuesta'
urlpatterns = [
    path('paenc1', index,name='pa1'),
   # path('pagenc2', mujer,name='pa2'),
    #path('pregunta/', mujer,name='pa3'),

    #path('perfil/<str:nombre>', primera_vista),
]
