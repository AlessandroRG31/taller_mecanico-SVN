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
        """
        Si la URL incluye cliente_id, lo preselecciona en el form igual que
        en MantenimientoCreateView con vehiculo.
        """
        initial = super().get_initial()
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            initial['cliente'] = cliente_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        cliente_id = self.kwargs.get('cliente_id')
        if cliente_id:
            # Preselecciona y desactiva el campo cliente si viene por URL
            form.fields['cliente'].initial = cliente_id
            form.fields['cliente'].queryset = form.fields['cliente'].queryset.filter(id=cliente_id)
            form.fields['cliente'].empty_label = None
        return form

    def form_valid(self, form):
        """
        Guardado idéntico al de MantenimientoCreateView: 
        form.save() en bloque y luego redirección.
        """
        # 1) Salvamos la instancia con todos los campos (incluido cliente)
        self.object = form.save()
        # 2) Redirigimos al success_url
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
        vehiculo_id = self.kwargs.get('vehiculo_id')
        if vehiculo_id:
            initial['vehiculo'] = vehiculo_id
        return initial

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['repuesto_formset'] = RepuestoMantenimientoFormSet(self.request.POST or None)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['repuesto_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))

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
        context = self.get_context_data()
        formset = context['repuesto_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))

class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')
