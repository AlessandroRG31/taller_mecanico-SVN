# Ruta: mantenimiento/urls.py

from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    # Vehículos
    path('vehiculos/', views.listar_vehiculos, name='vehiculo_list'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='vehiculo_nuevo'),

    # Mantenimientos
    # Ahora el listado vive en la raíz de /mantenimientos/
    path('', views.listar_mantenimientos, name='mantenimiento_list'),
    # Y el formulario en /mantenimientos/nuevo/
    path('nuevo/', views.crear_mantenimiento, name='mantenimiento_nuevo'),
    # Opción de crear mantenimiento desde un vehículo concreto
    path('nuevo/<int:vehiculo_id>/', views.crear_mantenimiento, name='mantenimiento_nuevo_con_vehiculo'),
]
