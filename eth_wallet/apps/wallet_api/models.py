from django.db import models


class Wallet(models.Model):
    CURRENCIES = (
        ('ETH', "ETH"),
    )

    currency = models.CharField(max_length=3, choices=CURRENCIES, verbose_name='Валюта', default="ETH")
    private_key = models.CharField(max_length=500, verbose_name="Приватный ключ")
    public_key = models.CharField(max_length=400, db_index=True, verbose_name='Публичный ключ')
    balance = models.FloatField(verbose_name='Баланс', default=0.0)

    def __repr__(self):
        return f'Wallet {self.id} (balance: {self.balance} {self.currency}) - {self.public_key}'

    class Meta:
        verbose_name = 'Кошелёк'
        verbose_name_plural = 'Кошельки'
        ordering = ['balance']
