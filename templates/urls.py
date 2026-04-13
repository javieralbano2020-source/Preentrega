from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('persona/', views.agregar_persona, name='form_persona'),
    path('ubicacion/', views.agregar_ubicacion, name='form_ubicacion'),
    path('evento/', views.agregar_evento, name='form_evento'),
    path('buscar/', views.buscar_evento, name='buscar_evento'),
]