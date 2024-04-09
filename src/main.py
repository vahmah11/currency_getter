import datetime
import time

from src.collector_filters.collector_by_interval import RatesCollectorByInterval
from src.collectors.rates_collector_abc import RatesCollector
from src.currency_saver import CurrencySaver
from src.dto import CurrencyStatusDTO


def get_currencies(
    currencies: list[str],
    collectors: list[RatesCollector],
) -> list[CurrencyStatusDTO]:
    result = []

    for collector in collectors:
        for currency in currencies:
            cur_value = collector.get_currency(currency)
            result.append(
                CurrencyStatusDTO(
                    currency,
                    cur_value,
                    datetime.datetime.now(),
                    collector.source_name()
                )
            )
    return result


def save(
    currency_savers: list[CurrencySaver],
    currencies: list[CurrencyStatusDTO]
):
    for currency_saver in currency_savers:
        for currency in currencies:
            currency_saver.save(currency)


def main():
    currencies = ['usd', 'euro']

    while True:
        collectors: list[RatesCollector] = RatesCollectorByInterval().get_collectors(
            datetime.datetime.now()
        )
        currencies_results = get_currencies(currencies, collectors)

        currency_savers = []
        save(currency_savers, currencies_results)
        time.sleep(400)


if __name__ == '__main__':
    main()
