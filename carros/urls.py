from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('carros/', views.lista_carros, name='lista-carros'),
    path('carros/<int:pk>/', views.detalhe_carro, name='detalhe-carro'),
    path('vendas/', views.lista_vendas, name='lista-vendas'),
    path('sobre-nos/', views.sobre_nos, name='sobre-nos'),
]