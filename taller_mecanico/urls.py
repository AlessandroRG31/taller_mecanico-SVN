from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('mantenimientos/', include(('mantenimiento.urls', 'mantenimiento'), namespace='mantenimiento')),
    path('repuestos/', include(('repuestos.urls', 'repuestos'), namespace='repuestos')),
    # Se remueven rutas genéricas de DAL para evitar ModuleNotFoundError:
    # path('autocomplete/', include('dal.urls')),
    # path('autocomplete/', include('dal_select2.urls')),
]

# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
