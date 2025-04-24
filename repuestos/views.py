from django.shortcuts import render
from .models import Repuesto

def buscar_repuestos(request):
    query = request.GET.get('q', '')
    qs = Repuesto.objects.select_related('empresa')
    if query:
        qs = qs.filter(nombre__icontains=query)
    orden = request.GET.get('orden', 'precio')
    qs = qs.order_by(orden)
    return render(request, 'repuestos/repuesto_search.html', {
        'resultados': qs,
        'query': query,
    })
