from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Evento, Persona, Ubicacion
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

def about(request):
    return render(request, 'about.html')

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Register
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Editar persona
def editar_persona(request, pk):
    persona = Persona.objects.get(id=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'form_persona.html', {'form': form})

# Eliminar persona
def eliminar_persona(request, pk):
    persona = Persona.objects.get(id=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('listar_personas')
    return render(request, 'confirmar_eliminar.html', {'objeto': persona})

# Listar personas
def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'listar_personas.html', {'personas': personas})

# Listar ubicaciones
def listar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'listar_ubicaciones.html', {'ubicaciones': ubicaciones})

# Editar ubicación
def editar_ubicacion(request, pk):
    ubicacion = Ubicacion.objects.get(id=pk)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('listar_ubicaciones')
    else:
        form = UbicacionForm(instance=ubicacion)
    return render(request, 'form_ubicacion.html', {'form': form})

# Eliminar ubicación
def eliminar_ubicacion(request, pk):
    ubicacion = Ubicacion.objects.get(id=pk)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('listar_ubicaciones')
    return render(request, 'confirmar_eliminar.html', {'objeto': ubicacion})

# Listar eventos
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})

# Editar evento
def editar_evento(request, pk):
    evento = Evento.objects.get(id=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'form_evento.html', {'form': form})

# Eliminar evento
def eliminar_evento(request, pk):
    evento = Evento.objects.get(id=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'confirmar_eliminar.html', {'objeto': evento})