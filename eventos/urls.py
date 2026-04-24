from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.form_persona, name='form_persona'),
    path('buscar/', views.buscar_evento, name='buscar_evento'),
    path('registrar-ubicacion/', views.form_ubicacion, name='form_ubicacion'),
    path('crear-evento/', views.form_evento, name='form_evento'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('personas/', views.listar_personas, name='listar_personas'),
    path('personas/editar/<int:pk>/', views.editar_persona, name='editar_persona'),
    path('personas/eliminar/<int:pk>/', views.eliminar_persona, name='eliminar_persona'),
    path('ubicaciones/', views.listar_ubicaciones, name='listar_ubicaciones'),
    path('ubicaciones/editar/<int:pk>/', views.editar_ubicacion, name='editar_ubicacion'),
    path('ubicaciones/eliminar/<int:pk>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
]
