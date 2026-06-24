from django.contrib import admin
from .models import Carro, Venda


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'disponivel')
    list_filter = ('disponivel', 'marca')
    search_fields = ('marca', 'modelo')


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'valor_venda', 'data_venda')
    search_fields = ('cliente', 'carro__modelo')
