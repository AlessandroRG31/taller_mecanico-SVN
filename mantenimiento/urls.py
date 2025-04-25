from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    # Listado de vehículos
    path('vehiculos/', views.listar_vehiculos, name='vehiculo_list'),
    # Detalle de vehículo
    path('vehiculos/<int:pk>/', views.detalle_vehiculo, name='vehiculo_detail'),
    # Nuevo vehículo
    path('vehiculos/nuevo/', views.crear_vehiculo, name='vehiculo_nuevo'),

    # Listado de mantenimientos
    path('', views.listar_mantenimientos, name='mantenimiento_list'),
    # Crear mantenimiento general
    path('nuevo/', views.crear_mantenimiento, name='mantenimiento_nuevo'),
    # Crear mantenimiento desde vehículo
    path('nuevo/<int:vehiculo_id>/', views.crear_mantenimiento, name='mantenimiento_nuevo_con_vehiculo'),
]
