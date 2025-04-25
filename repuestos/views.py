from django.shortcuts     import render
from django.core.paginator import Paginator
from .models              import Repuesto

def buscar_repuestos(request):
    qs = Repuesto.objects.select_related('empresa').filter(stock__gt=0)
    q  = request.GET.get('q', '')
    if q:
        qs = qs.filter(nombre__icontains=q)
    orden = request.GET.get('orden', 'precio')
    qs    = qs.order_by(orden)

    paginator   = Paginator(qs, 10)
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    return render(request, 'repuestos/repuesto_search.html', {
        'page_obj': page_obj,
        'q'       : q,
        'orden'   : orden,
    })
