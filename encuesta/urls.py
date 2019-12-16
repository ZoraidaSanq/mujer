from django.urls import path
from .views import (generar_reporte, index_reporte)

app_name='encuesta'
urlpatterns = [
    path('', index_reporte, name='index_reporte'),
    path('g_reporte/',generar_reporte, name='generar_reporte'),
    # path('generar/<str:nombre>/<int:pk>', generar_reporte,name='reporte')
   # path('pagenc2', mujer,name='pa2'),
    #path('pregunta/', mujer,name='pa3'),

    #path('perfil/<str:nombre>', primera_vista),
]
