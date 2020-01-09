from django.urls import path

from .views import (
    dashboard,
    registro_actividad, 
    registro_seguimiento,
    charts, 
    tables,
    cargar_caracteristicas,
    cargar_objetivos,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('actividades/', registro_actividad, name='registro_actividad'),
    path('seguimientos/', registro_seguimiento, name='registro_seguimiento'),
    path('charts/', charts, name='charts'),
    path('tables/', tables, name='tables'),

    #peticiones asincronas
    path('actividades/cargarcaracteristicas/<int:id_factor>/', cargar_caracteristicas, name='cargar_caracteristicas'),
    path('actividades/cargarobjetivos/<int:id_caracteristica>/', cargar_objetivos, name='cargar_objetivos'),


]