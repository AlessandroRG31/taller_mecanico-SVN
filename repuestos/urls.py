from django.urls import path
from .views import buscar_repuestos

app_name = 'repuestos'

urlpatterns = [
    # La ruta raíz de la app muestra la búsqueda
    path('', buscar_repuestos, name='buscar_repuestos'),
]
