from django.urls import path
from .views import landing, login_view, register_view, dashboard, logout_view

app_name = 'core'

urlpatterns = [
    # Página de inicio
    path('', landing, name='landing'),
    # Login / Logout / Registro
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    # Dashboard (requiere login)
    path('dashboard/', dashboard, name='dashboard'),
]
