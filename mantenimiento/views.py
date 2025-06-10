from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Vehiculo, Mantenimiento
from .forms import VehiculoForm, MantenimientoForm, RepuestoMantenimientoFormSet

# —— Vistas de Vehículo ——
class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_list.html'
    context_object_name = 'vehiculos'
    paginate_by = 10

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'mantenimiento/vehiculo_detail.html'
    context_object_name = 'vehiculo'

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'mantenimiento/vehiculo_form.html'
    success_url = reverse_lazy('mantenimiento:vehiculo-list')

    def form_valid(self, form):
        # Se asegura que el cliente sea enviado
        if not form.cleaned_data.get("cliente"):
            form.add_error("cliente", "Debe seleccionar un cliente.")
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


# —— Vistas de Mantenimiento con formset de repuestos ——
class MantenimientoListView(ListView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_list.html'
    context_object_name = 'mantenimientos'
    paginate_by = 10

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'mantenimiento/vehiculo_form.html'
    success_url = reverse_lazy('mantenimiento:vehiculo-list')

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not form.cleaned_data.get("cliente"):
            form.add_error("cliente", "Debe seleccionar un cliente.")
            return self.form_invalid(form)

        self.object = form.save(commit=False)
        self.object.cliente = form.cleaned_data["cliente"]
        self.object.save()
        form.save_m2m()
        return redirect(self.success_url)


class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['repuesto_formset'] = RepuestoMantenimientoFormSet(self.request.POST, instance=self.object)
        else:
            data['repuesto_formset'] = RepuestoMantenimientoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        repuesto_formset = context['repuesto_formset']
        if repuesto_formset.is_valid():
            self.object = form.save()
            repuesto_formset.instance = self.object
            repuesto_formset.save()
            return redirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form))

class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = 'mantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')
