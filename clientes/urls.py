from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    VehiculoCreateView,  # Nueva vista para Vehículo
)

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('nuevo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente-delete'),

    # Ruta “Nuevo Vehículo” recibiendo cliente_id
    path(
        'vehiculos/nuevo/<int:cliente_id>/',
        VehiculoCreateView.as_view(),
        name='vehiculo-create'
    ),
]
