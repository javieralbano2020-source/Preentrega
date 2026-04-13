from django import forms
from .models import Persona, Ubicacion, Evento

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'