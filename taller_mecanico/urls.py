from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('mantenimientos/', include(('mantenimiento.urls', 'mantenimiento'), namespace='mantenimiento')),
    path('repuestos/', include(('repuestos.urls', 'repuestos'), namespace='repuestos')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
