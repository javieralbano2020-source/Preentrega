from django.shortcuts import render, redirect
from .models import Evento
from .forms import PersonaForm, UbicacionForm, EventoForm

# Para la página principal
def home(request):
    return render(request, 'home.html')

# Para el buscador
def buscar_evento(request):
    query = request.GET.get('q')
    if query:
        resultados = Evento.objects.filter(nombre__icontains=query)
    else:
        resultados = []
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})

# Para registrar una persona
def form_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige al inicio si se guardó bien
    else:
        form = PersonaForm()
    return render(request, 'form_persona.html', {'form': form})

# Para registrar una ubicación
def form_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UbicacionForm()
    return render(request, 'form_ubicacion.html', {'form': form})

# Para crear un evento
def form_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventoForm()
    return render(request, 'form_evento.html', {'form': form})