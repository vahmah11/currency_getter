import datetime

from src.collectors.first_lib_collector import FirstLibRatesCollector
from src.collectors.rates_collector_abc import RatesCollector
from src.collectors.second_lib_collector import SecondLibRatesCollector
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
    collectors: list[RatesCollector] = [FirstLibRatesCollector(), SecondLibRatesCollector()]
    currencies_results = get_currencies(currencies, collectors)

    currency_savers = []
    save(currency_savers, currencies_results)



if __name__ == '__main__':
    main()
