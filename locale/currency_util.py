
from collections import OrderedDict
from .country_util import CountryUtil
from .locale_util import LocaleUtil, Locale
from .fiat_currency import FiatCurrency
from .language_util import LanguageUtil
import babel

class CurrencyUtil:
    @staticmethod
    def create_fiat_currency_map():
        # Get all countries
        all_countries = CountryUtil.get_all_countries()

        # Map and filter unique currencies
        fiat_currencies = {}
        for country in all_countries:
            currency = CountryUtil.get_currency_by_country_code(country.code)
            if currency.code not in fiat_currencies:
                fiat_currencies[currency.code] = currency

        # Sort the fiat currencies by their code and return as an OrderedDict
        sorted_fiat_currencies = OrderedDict(
            sorted(fiat_currencies.items(), key=lambda item: item[0])
        )

        return sorted_fiat_currencies
    
    @staticmethod
    def get_currency_by_country_code(country_code):
        if country_code == "XK":
            return FiatCurrency("EUR")  # Special case for Kosovo

        # Get default language for the country
        default_language = LanguageUtil.get_default_language()

        # Retrieve the currency instance based on locale
        try:
            locale = Locale(default_language, country_code)
            return FiatCurrency.from_country_code_locale(country_code, locale)
        except Exception as e:
            # Handle any exceptions, such as invalid country codes
            return None