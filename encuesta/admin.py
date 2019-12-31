from django.contrib import admin
from .models import (Encuesta,Pregunta,
Mujer, EncuestaMujer, Preguntaresultado,Likert)

admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(Mujer)
admin.site.register(EncuestaMujer)
admin.site.register(Preguntaresultado)
admin.site.register(Likert)