from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    # Vehículos
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('vehiculos/nuevo/<int:cliente_id>/', views.VehiculoCreateView.as_view(), name='vehiculo-create-por-cliente'),
    path('vehiculos/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo-detail'),
    path('vehiculos/editar/<int:pk>/', views.VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('vehiculos/eliminar/<int:pk>/', views.VehiculoDeleteView.as_view(), name='vehiculo-delete'),

    # Mantenimientos
    path('mantenimientos/', views.MantenimientoListView.as_view(), name='mantenimiento-list'),
    path('mantenimientos/nuevo/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('mantenimientos/nuevo/<int:vehiculo_id>/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create-por-vehiculo'),
    path('mantenimientos/editar/<int:pk>/', views.MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
    path('mantenimientos/eliminar/<int:pk>/', views.MantenimientoDeleteView.as_view(), name='mantenimiento-delete'),
]
