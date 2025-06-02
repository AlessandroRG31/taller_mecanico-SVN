# repuestos/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Empresa, Repuesto
from .forms import EmpresaForm, RepuestoForm

# ---------------------------------------------------
# Vista pública de búsqueda de repuestos (homepage)
def buscar_repuestos(request):
    orden = request.GET.get('orden', 'precio')
    if orden not in ['precio', '-precio', 'stock', '-stock', 'nombre', '-nombre']:
        orden = 'precio'
    repuestos = Repuesto.objects.select_related('empresa')\
                    .filter(stock__gt=0).order_by(orden)
    return render(request, 'repuestos/repuesto_search.html', {
        'repuestos': repuestos,
        'orden': orden,
    })


# ---------------------------------------------------
# CRUD Empresa
class EmpresaListView(ListView):
    model = Empresa
    template_name = 'repuestos/empresa_list.html'
    context_object_name = 'empresas'


class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'repuestos/empresa_form.html'
    success_url = reverse_lazy('repuestos:empresa_list')


class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'repuestos/empresa_form.html'
    success_url = reverse_lazy('repuestos:empresa_list')


class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'repuestos/empresa_confirm_delete.html'
    success_url = reverse_lazy('repuestos:empresa_list')


# ---------------------------------------------------
# CRUD Repuesto
class RepuestoListView(ListView):
    model = Repuesto
    template_name = 'repuestos/repuesto_list.html'
    context_object_name = 'repuestos'


class RepuestoCreateView(CreateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = 'repuestos/repuesto_form.html'
    success_url = reverse_lazy('repuestos:repuesto_list')


class RepuestoUpdateView(UpdateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = 'repuestos/repuesto_form.html'
    success_url = reverse_lazy('repuestos:repuesto_list')


class RepuestoDeleteView(DeleteView):
    model = Repuesto
    template_name = 'repuestos/repuesto_confirm_delete.html'
    success_url = reverse_lazy('repuestos:repuesto_list')
