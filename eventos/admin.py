from django.contrib import admin
from .models import Persona, Ubicacion, Evento

admin.site.register(Persona)
admin.site.register(Ubicacion)
admin.site.register(Evento)