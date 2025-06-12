from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from .forms import VehiculoForm, MantenimientoForm, RepuestoMantenimientoFormSet
from clientes.models import Cliente

# ============================
#   VISTAS DE VEHÍCULO
# ============================

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_list.html'
    context_object_name = 'vehiculos'
    paginate_by = 10
    ordering = ['placa']

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_detail.html'
    context_object_name = 'vehiculo'

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'mantenimiento/vehiculo_form.html'
    success_url = reverse_lazy('mantenimiento:vehiculo-list')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'mantenimiento/vehiculo_form.html'
    success_url = reverse_lazy('mantenimiento:vehiculo-list')

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:vehiculo-list')

# ============================
#   VISTAS DE MANTENIMIENTO
# ============================

class MantenimientoListView(ListView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_list.html'
    context_object_name = 'mantenimientos'
    ordering = ['-fecha_mantenimiento']
    
class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['repuestos'] = RepuestoMantenimientoFormSet(self.request.POST)
        else:
            context['repuestos'] = RepuestoMantenimientoFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        repuestos = context['repuestos']
        if form.is_valid() and repuestos.is_valid():
            self.object = form.save()
            repuestos.instance = self.object
            repuestos.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['repuestos'] = RepuestoMantenimientoFormSet(self.request.POST, instance=self.object)
        else:
            context['repuestos'] = RepuestoMantenimientoFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        repuestos = context['repuestos']
        if form.is_valid() and repuestos.is_valid():
            self.object = form.save()
            repuestos.instance = self.object
            repuestos.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

class MantenimientoCreateViewConVehiculo(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_initial(self):
        vehiculo_id = self.kwargs.get('vehiculo_id')
        return {'vehiculo': vehiculo_id}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['repuestos'] = RepuestoMantenimientoFormSet(self.request.POST)
        else:
            context['repuestos'] = RepuestoMantenimientoFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        repuestos = context['repuestos']
        if form.is_valid() and repuestos.is_valid():
            self.object = form.save()
            repuestos.instance = self.object
            repuestos.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
