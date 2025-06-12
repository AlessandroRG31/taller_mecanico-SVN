# ruta: taller_mecanico/core/urls.py

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',          views.landing,     name='landing'),
    path('login/',    views.login_view,  name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/',views.dashboard,   name='dashboard'),
    path('logout/',   views.logout_view, name='logout'),
]
