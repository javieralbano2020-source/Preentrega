from django.shortcuts import render
from .models import Evento

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

def form_persona(request):
    return render(request, 'form_persona.html')