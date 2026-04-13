from django.shortcuts import render
from .forms import PersonaForm, UbicacionForm, EventoForm
from .models import Evento

def inicio(request):
    return render(request, 'eventos_app/base.html')

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'eventos_app/base.html')
    else:
        form = PersonaForm()
    return render(request, 'eventos_app/form_persona.html', {'form': form})

# Repetir lógica similar para agregar_ubicacion y agregar_evento...

def buscar_evento(request):
    if request.GET.get('nombre'):
        nombre = request.GET.get('nombre')
        eventos = Evento.objects.filter(nombre__icontains=nombre)
        return render(request, 'eventos_app/resultado_busqueda.html', {'eventos': eventos})
    return render(request, 'eventos_app/buscar_evento.html')