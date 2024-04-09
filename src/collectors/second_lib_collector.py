from decimal import Decimal

from src.collectors.rates_collector_abc import RatesCollector
from src.outside_libs.second_lib import current_rates


class SecondLibRatesCollector(RatesCollector):
    def get_currency(self, cur: str) -> Decimal:
        return current_rates(cur)

    def source_name(self):
        return "second_lib"
