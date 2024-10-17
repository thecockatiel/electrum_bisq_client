
from ..proto.generated.pb_pb2 import Currency, CryptoCurrency, FiatCurrency as ProtoFiatCurrency
from babel.numbers import get_currency_name, get_territory_currencies
from .locale_util import Locale

class FiatCurrency():
    PREFIX = "★ "

    def __init__(self, code: str, crypto_currency: CryptoCurrency = None, fiat_currency: ProtoFiatCurrency = None, locale: Locale = None):
        self.code = code
        if locale:
            self.name = get_currency_name(code, locale=locale) 
        else:
            self.name = get_currency_name(code)
        self.crypto_currency = crypto_currency
        self.fiat_currency = fiat_currency

    def get_display_prefix(self):
        return self.PREFIX

    def to_proto_message(self):
        return Currency(self.code)

    @staticmethod
    def from_proto(proto):
        return FiatCurrency(proto['currency']['currency_code'])

    @staticmethod
    def get_display_prefix():
        return FiatCurrency.PREFIX
    
    @staticmethod
    def from_country_code_locale(country_code: str, locale: Locale):
        found_currency = get_territory_currencies(country_code)
        if (found_currency):
            return FiatCurrency(found_currency[0], locale)
        raise Exception("No currency found for country code: " + country_code)
    