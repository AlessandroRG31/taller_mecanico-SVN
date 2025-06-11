from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.shortcuts import get_object_or_404
from .models import Cliente
from mantenimiento.models import Vehiculo
from .forms import ClienteForm, VehiculoForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    ordering = ['id']

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('clientes:cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('clientes:cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes:cliente-list')

class VehiculoCreateView(CreateView):
    """
    “Nuevo Vehículo” idéntico al flujo de “Nuevo Mantenimiento”:
    preselecciona cliente_id y salva commit=False para evitar IntegrityError.
    """
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'clientes/vehiculo_form.html'
    success_url = reverse_lazy('clientes:cliente-list')

    def get_initial(self):
        initial = super().get_initial()
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            initial['cliente'] = cliente_id
        return initial

    def form_valid(self, form):
        veh = form.save(commit=False)
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            veh.cliente_id = cliente_id
        veh.save()
        return super().form_valid(form)
