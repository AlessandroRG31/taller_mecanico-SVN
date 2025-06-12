from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Vehiculo, Mantenimiento
from .forms import VehiculoForm, MantenimientoForm, RepuestoMantenimientoFormSet

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_list.html'

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

    def form_valid(self, form):
        # Detener el save automático para inyectar FK
        cliente_id = self.kwargs.get('cliente_id')
        veh = form.save(commit=False)
        if cliente_id:
            veh.cliente_id = cliente_id
        veh.save()
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

class MantenimientoListView(ListView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_list.html'

class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_initial(self):
        initial = super().get_initial()
        vehiculo_id = self.kwargs.get('vehiculo_id')
        if vehiculo_id:
            initial['vehiculo'] = vehiculo_id
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['repuesto_formset'] = RepuestoMantenimientoFormSet(
            self.request.POST or None,
            instance=self.object
        )
        return data

    def form_valid(self, form):
        vehiculo_id = self.kwargs.get('vehiculo_id')
        mant = form.save(commit=False)
        if vehiculo_id:
            mant.vehiculo_id = vehiculo_id
        mant.save()
        formset = self.get_context_data()['repuesto_formset']
        if formset.is_valid():
            formset.instance = mant
            formset.save()
        return super().form_valid(form)

class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')
