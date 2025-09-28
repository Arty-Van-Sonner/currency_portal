from .models import Currency
from django.db import models

class CurrencyNameOption(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    option_key = models.CharField(max_length=256)
