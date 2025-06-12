from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    # Ruta nueva para recibir cliente_id y preseleccionar la FK
    path('vehiculos/nuevo/<int:cliente_id>/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    
    path('mantenimientos/', views.MantenimientoListView.as_view(), name='mantenimiento-list'),
    path('mantenimientos/nuevo/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('mantenimientos/nuevo/<int:vehiculo_id>/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
]
