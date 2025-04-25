# mantenimiento/views.py

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
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('placa')
    return render(request, 'mantenimiento/vehiculo_list.html', {'vehiculos': vehiculos})

@login_required
def detalle_vehiculo(request, pk):
    veh = get_object_or_404(Vehiculo, pk=pk)
    prox = veh.proximos.order_by('fecha_programada').first()
    return render(request, 'mantenimiento/vehiculo_detail.html', {
        'vehiculo': veh,
        'proximo': prox,
    })

@login_required
def crear_vehiculo(request):
    if request.method == 'POST':
        veh_form = VehiculoForm(request.POST, request.FILES)
        prox_form = ProximoMantenimientoForm(request.POST)
        if veh_form.is_valid() and prox_form.is_valid():
            veh = veh_form.save()
            prox = prox_form.save(commit=False)
            prox.vehiculo = veh
            prox.save()
            return redirect('mantenimiento:vehiculo_list')
    else:
        veh_form = VehiculoForm()
        prox_form = ProximoMantenimientoForm()
    return render(request, 'mantenimiento/vehiculo_form.html', {
        'vehiculo_form': veh_form,
        'proximomantenimiento_form': prox_form
    })

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
            formset = RepuestoMantenimientoFormSet(request.POST, instance=mant)
            if formset.is_valid():
                formset.save()
                return redirect('mantenimiento:mantenimiento_list')
        else:
            formset = RepuestoMantenimientoFormSet(request.POST)
    else:
        initial = {'vehiculo': vehiculo.id} if vehiculo else {}
        form = MantenimientoForm(initial=initial)
        formset = RepuestoMantenimientoFormSet()

    return render(request, 'mantenimiento/mantenimiento_form.html', {
        'form': form,
        'formset': formset,
        'vehiculo': vehiculo
    })
