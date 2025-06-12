from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.cliente_list, name='cliente-list'),
    path('nuevo/', views.cliente_create, name='cliente-create'),
    path('<int:pk>/editar/', views.cliente_update, name='cliente-update'),
]
