from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # Montamos la app de Mantenimiento en /mantenimientos/
    path('mantenimientos/', include('mantenimiento.urls', namespace='mantenimiento')),
    # Montamos la app de Repuestos en /repuestos/
    path('repuestos/', include('repuestos.urls', namespace='repuestos')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
