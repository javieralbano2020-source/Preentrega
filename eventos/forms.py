from django import forms
from .models import Persona, Ubicacion, Evento

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'