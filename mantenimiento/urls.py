from django.urls import path, include
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('vehiculos/nuevo/<int:cliente_id>/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),

    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo-delete'),

    path('mantenimientos/', views.MantenimientoListView.as_view(), name='mantenimiento-list'),
    path('mantenimientos/nuevo/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('mantenimientos/nuevo/<int:vehiculo_id>/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
    path('mantenimientos/<int:pk>/editar/', views.MantenimientoUpdateView.as_view(), name='mantenimiento-update'),
    path('mantenimientos/<int:pk>/eliminar/', views.MantenimientoDeleteView.as_view(), name='mantenimiento-delete'),
]