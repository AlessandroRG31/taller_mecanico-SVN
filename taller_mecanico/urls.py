from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('mantenimiento/', include('mantenimiento.urls', namespace='mantenimiento')),
    path('repuestos/', include('repuestos.urls', namespace='repuestos')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
