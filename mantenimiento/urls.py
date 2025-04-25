# Ruta: mantenimiento/urls.py

from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    # Vehículos
    path('vehiculos/', views.listar_vehiculos, name='vehiculo_list'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='vehiculo_nuevo'),

    # Mantenimientos
    path('', views.listar_mantenimientos, name='mantenimiento_list'),
    path('nuevo/', views.crear_mantenimiento, name='mantenimiento_nuevo'),
    path('nuevo/<int:vehiculo_id>/', views.crear_mantenimiento, name='mantenimiento_nuevo_con_vehiculo'),
]
