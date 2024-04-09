from decimal import Decimal

from src.collectors.rates_collector_abc import RatesCollector
from src.outside_libs.first_lib import get_rates


class FirstLibRatesCollector(RatesCollector):
    def get_currency(self, cur: str) -> Decimal:
        return get_rates().get('result')

    def source_name(self):
        return "first_lib"
