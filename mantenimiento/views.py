from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Vehiculo, Mantenimiento
from .forms import VehiculoForm, MantenimientoForm

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_list.html'
    context_object_name = 'vehiculos'

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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Solo ocultar el campo si VIENE cliente_id en la URL
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            form.fields['cliente'].widget = forms.HiddenInput()
        else:
            form.fields['cliente'].widget = forms.Select()
        return form

    def form_valid(self, form):
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            form.instance.cliente_id = cliente_id
        # Validar de nuevo antes de guardar
        if not form.instance.cliente_id:
            form.add_error('cliente', "Debes seleccionar un cliente.")
            return self.form_invalid(form)
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

    def form_valid(self, form):
        vehiculo_id = self.kwargs.get('vehiculo_id')
        if vehiculo_id:
            form.instance.vehiculo_id = vehiculo_id
        return super().form_valid(form)
