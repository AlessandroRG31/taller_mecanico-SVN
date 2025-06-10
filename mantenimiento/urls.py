# mantenimiento/urls.py

from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('vehiculos/', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('mantenimientos/', views.MantenimientoListView.as_view(), name='mantenimiento-list'),
    path('mantenimientos/nuevo/', views.MantenimientoCreateView.as_view(), name='mantenimiento-create'),
]
