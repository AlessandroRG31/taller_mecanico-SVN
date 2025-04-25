from django.urls import path
from .views      import buscar_repuestos

app_name = 'repuestos'

urlpatterns = [
    path('', buscar_repuestos, name='buscar_repuestos'),
]
