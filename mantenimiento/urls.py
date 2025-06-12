from django.urls import path
from .views import (
    VehiculoListView,
    VehiculoCreateView,
    VehiculoUpdateView,
    VehiculoDeleteView,
    MantenimientoCreateView,
    MantenimientoListView,
    MantenimientoUpdateView,
    MantenimientoDeleteView,
)

app_name = 'mantenimiento'

urlpatterns = [
    # ==== Vehículos ====
    # Listado de vehículos
    path('vehiculos/', VehiculoListView.as_view(), name='vehiculo-list'),
    # Crear vehículo (select de cliente)
    path('vehiculos/nuevo/', VehiculoCreateView.as_view(), name='vehiculo-create'),
    # Crear vehículo para un cliente preseleccionado
    path('vehiculos/nuevo/<int:cliente_id>/', VehiculoCreateView.as_view(), name='vehiculo-create-cliente'),
    # Editar vehículo
    path('vehiculos/editar/<int:pk>/', VehiculoUpdateView.as_view(), name='vehiculo-update'),
    # Eliminar vehículo
    path('vehiculos/eliminar/<int:pk>/', VehiculoDeleteView.as_view(), name='vehiculo-delete'),

    # ==== Mantenimientos ====
    # Listado de mantenimientos
    path('mantenimientos/', MantenimientoListView.as_view(), name='mantenimiento-list'),
    # Crear mantenimiento (select de vehículo)
    path('mantenimientos/nuevo/', MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    # Crear mantenimiento para un vehículo preseleccionado
    path(
        'mantenimientos/nuevo/vehiculo/<int:vehiculo_id>/',
        MantenimientoCreateView.as_view(),
        name='mantenimiento_nuevo_con_vehiculo'
    ),
    # Editar mantenimiento
    path('mantenimientos/editar/<int:pk>/', MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
    # Eliminar mantenimiento
    path('mantenimientos/eliminar/<int:pk>/', MantenimientoDeleteView.as_view(), name='mantenimiento-delete'),
]
