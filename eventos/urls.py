from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.form_persona, name='form_persona'),
    path('buscar/', views.buscar_evento, name='buscar_evento'),
    path('registrar-ubicacion/', views.form_ubicacion, name='form_ubicacion'),
    path('crear-evento/', views.form_evento, name='form_evento'),
]
