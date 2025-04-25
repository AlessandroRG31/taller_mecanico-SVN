from django.urls import path
from . import views

app_name = 'repuestos'

urlpatterns = [
    path('', views.buscar_repuestos, name='buscar_repuestos'),

    path('empresas/', views.EmpresaListView.as_view(), name='empresa_list'),
    path('empresa/nuevo/', views.EmpresaCreateView.as_view(), name='empresa_nuevo'),
    path('empresa/<int:pk>/editar/', views.EmpresaUpdateView.as_view(), name='empresa_editar'),
    path('empresa/<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='empresa_eliminar'),

    path('repuestos/', views.RepuestoListView.as_view(), name='repuesto_list'),
    path('repuesto/nuevo/', views.RepuestoCreateView.as_view(), name='repuesto_nuevo'),
    path('repuesto/<int:pk>/editar/', views.RepuestoUpdateView.as_view(), name='repuesto_editar'),
    path('repuesto/<int:pk>/eliminar/', views.RepuestoDeleteView.as_view(), name='repuesto_eliminar'),
]
