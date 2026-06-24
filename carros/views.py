from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render
from .models import Carro, Venda


def home(request):
    carros = Carro.objects.filter(disponivel=True).order_by('-created_at')[:6]
    vendas = Venda.objects.select_related('carro').order_by('-data_venda')[:5]
    return render(request, 'index.html', {
        'carros': carros,
        'vendas': vendas,
    })


def lista_carros(request):
    carros = Carro.objects.all().order_by('-created_at')
    return render(request, 'carros/lista.html', {
        'carros': carros,
    })


def detalhe_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    return render(request, 'carros/detalhe.html', {
        'carro': carro,
    })


@staff_member_required
def lista_vendas(request):
    vendas = Venda.objects.select_related('carro').order_by('-data_venda')
    return render(request, 'vendas/lista.html', {
        'vendas': vendas,
    })


def sobre_nos(request):
    return render(request, 'sobre_nos.html')