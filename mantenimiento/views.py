from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Vehiculo, Mantenimiento, ProximoMantenimiento
from .forms import (
    VehiculoForm,
    ProximoMantenimientoForm,
    MantenimientoForm,
    RepuestoMantenimientoFormSet,
)

@login_required
def listar_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.select_related('vehiculo') \
        .all().order_by('-fecha_mantenimiento')
    return render(request, 'mantenimiento/mantenimiento_list.html', {
        'mantenimientos': mantenimientos
    })

@login_required
def crear_mantenimiento(request, vehiculo_id=None):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id) if vehiculo_id else None

    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            mant = form.save(commit=False)
            if vehiculo:
                mant.vehiculo = vehiculo
            mant.save()
            # ahora instanciamos el formset sobre la instancia guardada
            formset = RepuestoMantenimientoFormSet(request.POST, instance=mant)
            if formset.is_valid():
                formset.save()
                return redirect('mantenimiento:mantenimiento_list')
        else:
            formset = RepuestoMantenimientoFormSet(request.POST)
    else:
        # GET: formularios vacíos
        initial = {'vehiculo': vehiculo.id} if vehiculo else {}
        form = MantenimientoForm(initial=initial)
        formset = RepuestoMantenimientoFormSet()

    return render(request, 'mantenimiento/mantenimiento_form.html', {
        'form': form,
        'formset': formset,
        'vehiculo': vehiculo
    })
