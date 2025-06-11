# taller_mecanico/mantenimiento/forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from dal import autocomplete
from datetime import date
from .models import Vehiculo, ProximoMantenimiento, Mantenimiento, RepuestoMantenimiento
from clientes.models import Cliente

class VehiculoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        label="Cliente",
        error_messages={'required': 'Debe seleccionar un cliente.'}
    )

    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'fecha_proxima_revision': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo <= 0:
            raise ValidationError("El costo del mantenimiento debe ser mayor que 0.")
        return costo

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }

RepuestoMantenimientoFormSet = inlineformset_factory(
    Mantenimiento,
    RepuestoMantenimiento,
    fields=('repuesto', 'cantidad'),
    extra=1,
    can_delete=True,
    widgets={'cantidad': forms.NumberInput(attrs={'min': 1})},
)

# taller_mecanico/mantenimiento/views.py

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

    def form_valid(self, form):
        cliente = form.cleaned_data.get("cliente")
        if not cliente:
            form.add_error("cliente", "Debe seleccionar un cliente.")
            return self.form_invalid(form)

        self.object = form.save(commit=False)
        self.object.cliente = cliente
        self.object.save()
        return redirect(self.success_url)

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
    ordering = ['-fecha_mantenimiento']

class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento:mantenimiento-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['repuesto_formset'] = RepuestoMantenimientoFormSet(self.request.POST)
        else:
            data['repuesto_formset'] = RepuestoMantenimientoFormSet()
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
