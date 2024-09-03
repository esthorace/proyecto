from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'clientes'


urlpatterns = [
    path('', views.index, name='index'),
    path('pais/list', login_required(views.pais_list), name='pais_list'),
    path('pais/create', login_required(views.pais_create), name='pais_create'),
    path('pais/detail/<int:pk>', login_required(views.pais_detail), name='pais_detail'),
    path('cliente/list', login_required(views.cliente_list), name='cliente_list'),
    path('cliente/create', login_required(views.cliente_create), name='cliente_create'),
]
