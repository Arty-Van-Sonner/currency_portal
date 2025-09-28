from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=256)
    international_name = models.CharField(max_length=256)
    local_name = models.CharField(max_length=256)

class CurrencyIssuer(models.Model):
    name = models.CharField(max_length=256)
    countries = models.ManyToManyField(Country, related_name='currency_issuers')

class Currency(models.Model):
    issuer = models.ForeignKey(CurrencyIssuer, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, help_text='Full name of the currency. For example: "United States Dollar"', default='Test')
    currency_code = models.CharField(max_length=3, unique=True, db_index=True, help_text='ISO 4217. It is a three-letter code. For example: "USD"')
    numeric_code = models.IntegerField(unique=True, db_index=True, help_text='ISO 4217. It is a three-digit numeric currency code. For example: 840')
    symbol = models.CharField(max_length=5, blank=True, help_text='A currency symbol. For example: "$"')
    is_active = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.code
    
    @property
    def information(self):
        '''
        self - <class 'Currency'> - object of this class
        '''
        information = f'''*Currency {self.name} ({self.international_designation})*:
    •	*International code:* {self.code};
    •	*Name:* {self.name};
    •	*International designation:* {self.international_designation};
    •	*Country:* {self.country}
    •	*Currency name options:* {self.currency_name_options}'''
        return information
    

