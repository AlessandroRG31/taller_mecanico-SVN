# taller_mecanico/core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'core/home.html')


def login_view(request):
    # Si ya está autenticado, lleva al dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        error = "Usuario o contraseña inválidos."
    else:
        form  = AuthenticationForm()
        error = None

    return render(request, 'core/login.html', {
        'form':  form,
        'error': error
    })


def register_view(request):
    # Si ya está autenticado, lleva al dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {
        'form': form
    })


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('landing')
