from datetime import datetime

from src.collectors.first_lib_collector import FirstLibRatesCollector
from src.collectors.rates_collector_abc import RatesCollector
from src.collectors.second_lib_collector import SecondLibRatesCollector


class RatesCollectorByInterval:
    hour_intervals = {
        (22, 6): [FirstLibRatesCollector],
        (6, 22): [SecondLibRatesCollector]
    }

    def get_collectors(
        self,
        current: datetime,
    ) -> list[RatesCollector]:

        for hour_interval, collectors in self.hour_intervals.items():
            start = datetime.now().replace(hour=hour_interval[0])
            end = datetime.now().replace(hour=hour_interval[1])

            if start <= current.replace(hour=hour_interval[0]) <= end:
                return collectors

        return []
