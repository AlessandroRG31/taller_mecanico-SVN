from django.urls import path
from .views import (
    VehiculoListView,
    VehiculoDetailView,
    VehiculoCreateView,
    VehiculoUpdateView,
    VehiculoDeleteView,
    MantenimientoListView,
    MantenimientoCreateView,
    MantenimientoUpdateView,
    MantenimientoDeleteView,
)

app_name = 'mantenimiento'

urlpatterns = [
    # Vehículos
    path('vehiculos/', VehiculoListView.as_view(), name='vehiculo-list'),
    # Ruta para Nuevo Vehículo SIN cliente_id (para el Dashboard)
    path('vehiculos/nuevo/', VehiculoCreateView.as_view(), name='vehiculo-create'),
    # Ruta para Nuevo Vehículo CON cliente_id (si venimos desde Detalle de Cliente)
    path('vehiculos/nuevo/<int:cliente_id>/', VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('vehiculos/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo-detail'),
    path('vehiculos/<int:pk>/editar/', VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('vehiculos/<int:pk>/eliminar/', VehiculoDeleteView.as_view(), name='vehiculo-delete'),

    # Mantenimientos
    path('mantenimientos/', MantenimientoListView.as_view(), name='mantenimiento-list'),
    path('mantenimientos/nuevo/<int:vehiculo_id>/', MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('mantenimientos/<int:pk>/editar/', MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
    path('mantenimientos/<int:pk>/eliminar/', MantenimientoDeleteView.as_view(), name='mantenimiento-delete'),
]
