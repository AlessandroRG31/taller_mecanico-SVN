from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .models import Vehiculo, Mantenimiento
from .forms import VehiculoForm, MantenimientoForm, RepuestoMantenimientoFormSet

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
        if cliente_id := self.kwargs.get('cliente_id'):
            initial['cliente'] = cliente_id
        return initial

    def form_valid(self, form):
        # Creamos la instancia sin guardar todavía
        veh = form.save(commit=False)

        # Si la URL trae cliente_id, lo asignamos; sino, usamos el valor del formulario
        if cliente_id := self.kwargs.get('cliente_id'):
            veh.cliente_id = cliente_id
        else:
            veh.cliente = form.cleaned_data.get('cliente')

        # Guardamos la instancia con cliente siempre asignado
        veh.save()
        # Continuamos con el flujo normal de CreateView
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
    context_object_name = 'mantenimientos'
    paginate_by = 10
    ordering = ['-fecha_mantenimiento']

class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_initial(self):
        initial = super().get_initial()
        if vehiculo_id := self.kwargs.get('vehiculo_id'):
            initial['vehiculo'] = vehiculo_id
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['repuesto_formset'] = RepuestoMantenimientoFormSet(self.request.POST or None)
        return data

    def form_valid(self, form):
        # Igual que en Vehiculo: asignamos siempre vehiculo
        if vehiculo_id := self.kwargs.get('vehiculo_id'):
            form.instance.vehiculo_id = vehiculo_id
        else:
            form.instance.vehiculo = form.cleaned_data.get('vehiculo')

        self.object = form.save()
        formset = self.get_context_data()['repuesto_formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

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
        self.object = form.save()
        formset = self.get_context_data()['repuesto_formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')
