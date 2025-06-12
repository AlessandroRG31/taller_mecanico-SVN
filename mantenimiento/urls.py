from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    # Vista sin cliente preseleccionado
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    # Vista con cliente preseleccionado (pasa cliente_id en la URL)
    path('vehiculos/nuevo/<int:cliente_id>/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('vehiculos/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo-detail'),
    path('vehiculos/editar/<int:pk>/', views.VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('vehiculos/eliminar/<int:pk>/', views.VehiculoDeleteView.as_view(), name='vehiculo-delete'),

    path('mantenimientos/', views.MantenimientoListView.as_view(), name='mantenimiento-list'),
    # Vista sin vehículo preseleccionado
    path('mantenimientos/nuevo/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    # Vista con vehículo preseleccionado (pasa vehiculo_id en la URL)
    path('mantenimientos/nuevo/<int:vehiculo_id>/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('mantenimientos/editar/<int:pk>/', views.MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
    path('mantenimientos/eliminar/<int:pk>/', views.MantenimientoDeleteView.as_view(), name='mantenimiento-delete'),
]
