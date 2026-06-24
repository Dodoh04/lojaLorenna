from django.db import models


class Carro(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=150, verbose_name='Modelo')
    ano = models.PositiveIntegerField(verbose_name='Ano')
    km = models.PositiveIntegerField(verbose_name='Quilometragem')
    cor = models.CharField(max_length=50, verbose_name='Cor', blank=True)
    combustivel = models.CharField(max_length=50, verbose_name='Combustível', blank=True)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Preço')
    imagem = models.ImageField(upload_to='carros/', verbose_name='Imagem', blank=True, null=True)
    disponivel = models.BooleanField(default=True, verbose_name='Disponível')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.marca} {self.modelo}'


class Venda(models.Model):
    carro = models.ForeignKey(
        Carro,
        on_delete=models.PROTECT,
        related_name='vendas',
        verbose_name='Carro'
    )
    cliente = models.CharField(max_length=200, verbose_name='Cliente')
    valor_venda = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Valor da venda'
    )
    data_venda = models.DateField(auto_now_add=True, verbose_name='Data da venda')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_venda']
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return f'{self.cliente} - {self.carro}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.carro.disponivel:
            self.carro.disponivel = False
            self.carro.save(update_fields=['disponivel'])
