from django.contrib import admin
from .models import (Encuesta, Likert, Pregunta,
Mujer, EncuestaMujer, Preguntaresultado,
Factorviolencia)

admin.site.register(Encuesta)
admin.site.register(Likert)
admin.site.register(Pregunta)
admin.site.register(Mujer)
admin.site.register(EncuestaMujer)
admin.site.register(Preguntaresultado)
admin.site.register(Factorviolencia)
