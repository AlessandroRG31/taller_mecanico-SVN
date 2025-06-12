from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from .forms import VehiculoForm, MantenimientoForm

# ... otras vistas ...

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "mantenimiento/vehiculo_form.html"
    success_url = reverse_lazy('mantenimiento:vehiculo-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            form.fields['cliente'].queryset = form.fields['cliente'].queryset.filter(id=cliente_id)
            form.fields['cliente'].initial = cliente_id
            form.fields['cliente'].widget.attrs['readonly'] = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_id'] = self.kwargs.get('cliente_id')
        return context

    def form_valid(self, form):
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            # Si llega cliente_id por la URL, lo asignamos manualmente
            cliente = get_object_or_404(form.fields['cliente'].queryset.model, id=cliente_id)
            form.instance.cliente = cliente
        # Si no, deja que el formulario asigne el cliente por el campo select normal
        return super().form_valid(form)
