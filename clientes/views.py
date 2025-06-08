from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from dal import autocomplete
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('clientes:list')

class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Cliente.objects.all()
        if self.q:
            qs = qs.filter(nombre__icontains=self.q) | qs.filter(apellido__icontains=self.q) | qs.filter(dui__icontains=self.q)
        return qs
