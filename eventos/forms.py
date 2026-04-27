from django import forms
from .models import Persona, Ubicacion, Evento

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control',}),
            'apellido': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
        }

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control',}),
            'direccion': forms.TextInput(attrs={'class': 'form-control',}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control',}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control',}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ubicacion': forms.Select(attrs={'class': 'form-select'}),
            'asistentes': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }