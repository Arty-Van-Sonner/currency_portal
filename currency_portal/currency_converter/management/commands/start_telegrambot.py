from django.core.management.base import BaseCommand
from models import Currency, CurrencyNameOption
from currencies.models import Country, CurrencyIssuer
from currency_converter.telegtambot import start_telegrambot

class Command(BaseCommand):
    def handle(self, *args, **options):
        start_telegrambot(*args, **options)