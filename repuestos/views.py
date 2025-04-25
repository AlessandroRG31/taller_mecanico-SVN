# repuestos/views.py

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Repuesto

def buscar_repuestos(request):
    # 1) Solo stock > 0
    qs = Repuesto.objects.select_related('empresa').filter(stock__gt=0)

    # 2) Filtrado por nombre
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(nombre__icontains=q)

    # 3) Orden por precio (ascendente por defecto)
    orden = request.GET.get('orden', 'precio')
    qs = qs.order_by(orden)

    # 4) Paginación
    paginator = Paginator(qs, 10)  # 10 repuestos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'repuestos/repuesto_search.html', {
    'resultados': qs,
    'query': query,
})

