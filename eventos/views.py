from django.shortcuts import render

from django.shortcuts import render
from .models import Evento

def buscar_evento(request):
    if request.GET.get('nombre'):
        nombre_buscado = request.GET.get('nombre')
        # Buscamos eventos que contengan ese nombre
        resultados = Evento.objects.filter(nombre__icontains=nombre_buscado)
        return render(request, 'eventos/resultados.html', {'eventos': resultados})
    
    return render(request, 'eventos/buscar.html')