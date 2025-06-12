from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin de Django
    path('admin/', admin.site.urls),

    # URLs de la app core (landing, login, register, dashboard, logout)
    path('', include(('core.urls', 'core'), namespace='core')),

    # URLs para clientes
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),

    # URLs para mantenimientos
    path('mantenimientos/', include(('mantenimiento.urls', 'mantenimiento'), namespace='mantenimiento')),

    # URLs para repuestos
    path('repuestos/', include(('repuestos.urls', 'repuestos'), namespace='repuestos')),
]

# URLs para archivos media en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
