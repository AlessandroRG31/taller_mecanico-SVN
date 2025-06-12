# taller_mecanico-SVN/mantenimiento/views.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.shortcuts import get_object_or_404
from .models import Vehiculo, Mantenimiento
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

    def get_initial(self):
        initial = super().get_initial()
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            initial['cliente'] = cliente_id
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            if self.request.method == 'GET':
                # Preselecciona en el form por GET
                kwargs.setdefault('initial', {})['cliente'] = cliente_id
            elif self.request.method == 'POST':
                # Fuerza el cliente de la URL en POST
                data = kwargs['data'].copy()
                data['cliente'] = cliente_id
                kwargs['data'] = data
        return kwargs

    def form_valid(self, form):
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            form.instance.cliente_id = cliente_id
        return super().form_valid(form)


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
    paginate_by = 10
    ordering = ['-fecha_mantenimiento']


class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def dispatch(self, request, *args, **kwargs):
        # Si viene vehiculo_id en la URL, lo guardamos para uso posterior
        self.vehiculo_obj = None
        vehiculo_id = kwargs.get('vehiculo_id')
        if vehiculo_id:
            self.vehiculo_obj = get_object_or_404(Vehiculo, pk=vehiculo_id)
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        if self.vehiculo_obj:
            initial['vehiculo'] = self.vehiculo_obj.pk
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.vehiculo_obj:
            # Oculta el select para forzar el vehículo de la URL
            form.fields['vehiculo'].widget = form.fields['vehiculo'].hidden_widget()
        return form

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['repuesto_formset'] = RepuestoMantenimientoFormSet(
            self.request.POST or None,
            instance=getattr(self, 'object', None)
        )
        return data

    def form_valid(self, form):
        # Asignamos el vehículo preseleccionado antes de guardar
        if self.vehiculo_obj:
            form.instance.vehiculo = self.vehiculo_obj
        response = super().form_valid(form)
        # Guardar el formset solo si es válido
        formset = self.get_context_data()['repuesto_formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return response


class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['repuesto_formset'] = RepuestoMantenimientoFormSet(
            self.request.POST or None,
            instance=self.object
        )
        return data

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = self.get_context_data()['repuesto_formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return response


class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')
