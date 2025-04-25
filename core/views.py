from django.shortcuts        import render, redirect
from django.contrib.auth     import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def landing(request):
    return render(request, 'core/landing.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('core:dashboard')
        else:
            error = "Credenciales inválidas"
            return render(request, 'core/login.html', {'error': error})
    return render(request, 'core/login.html')

@login_required
def dashboard(request):
    # aquí puedes añadir contexto: links a vehiculos/mantenimientos/repuestos
    return render(request, 'core/dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('core:landing')
