from django.urls import path
from .views import (
    VehiculoListView, VehiculoDetailView, VehiculoCreateView,
    VehiculoUpdateView, VehiculoDeleteView,
    MantenimientoListView, MantenimientoCreateView, MantenimientoUpdateView,
    MantenimientoDeleteView, MantenimientoCreateViewConVehiculo
)
from .import views

app_name = 'mantenimiento'

urlpatterns = [
    # Vehículos
    path('vehiculos/', VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculos/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo-detail'),
    path('vehiculos/nuevo/', VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('vehiculos/editar/<int:pk>/', VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('vehiculos/eliminar/<int:pk>/', VehiculoDeleteView.as_view(), name='vehiculo-delete'),

    # Mantenimientos
    path('', MantenimientoListView.as_view(), name='mantenimiento-list'),
    path('nuevo/', MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('editar/<int:pk>/', MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
    path('eliminar/<int:pk>/', MantenimientoDeleteView.as_view(), name='mantenimiento-delete'),

    # Mantenimiento con vehículo preseleccionado
    path('nuevo/<int:vehiculo_id>/', MantenimientoCreateViewConVehiculo.as_view(), name='mantenimiento_nuevo_con_vehiculo'),
    path('mantenimientos/nuevo/<int:vehiculo_id>/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create-with-vehiculo'),
]
