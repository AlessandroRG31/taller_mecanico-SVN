# Ruta: taller_mecanico/mantenimiento/urls.py
from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('vehiculos/', views.listar_vehiculos,    name='vehiculo_list'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='vehiculo_nuevo'),
    path('mantenimientos/', views.listar_mantenimientos, name='mantenimiento_list'),
    path('mantenimientos/nuevo/', views.crear_mantenimiento, name='mantenimiento_nuevo'),
    path('mantenimientos/nuevo/<int:vehiculo_id>/', views.crear_mantenimiento, name='mantenimiento_nuevo_con_vehiculo'),
]


