from django.urls import path
from .views import (
    EmpresaListView, EmpresaCreateView, EmpresaUpdateView, EmpresaDeleteView,
    RepuestoListView, RepuestoCreateView, RepuestoUpdateView, RepuestoDeleteView,
    buscar_repuestos
)

app_name = 'repuestos'

urlpatterns = [
    # EMPRESAS
    path('empresas/', EmpresaListView.as_view(), name='empresa-list'),
    path('empresas/nueva/', EmpresaCreateView.as_view(), name='empresa-create'),
    path('empresas/editar/<int:pk>/', EmpresaUpdateView.as_view(), name='empresa-update'),
    path('empresas/eliminar/<int:pk>/', EmpresaDeleteView.as_view(), name='empresa-delete'),

    # REPUESTOS
    path('', RepuestoListView.as_view(), name='repuesto_list'),
    path('nuevo/', RepuestoCreateView.as_view(), name='repuesto_nuevo'),
    path('editar/<int:pk>/', RepuestoUpdateView.as_view(), name='repuesto_editar'),
    path('eliminar/<int:pk>/', RepuestoDeleteView.as_view(), name='repuesto_eliminar'),

    # Búsqueda
    path('buscar/', buscar_repuestos, name='buscar_repuestos'),
]
