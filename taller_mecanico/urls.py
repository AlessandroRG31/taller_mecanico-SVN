from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URLs de la app core (landing, login, register, dashboard, logout)
    path('', include(('core.urls', 'core'), namespace='core')),

    # Sección de clientes
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),

    # Sección de mantenimientos
    path('mantenimientos/', include(('mantenimiento.urls', 'mantenimiento'), namespace='mantenimiento')),

    # Sección de repuestos (si existe)
    path('repuestos/', include(('repuestos.urls', 'repuestos'), namespace='repuestos')),

    # Admin de Django
    path('admin/', admin.site.urls),
]
