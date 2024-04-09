from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Optional


class RatesCollector(ABC):
    @abstractmethod
    def get_currency(self, cur: str) -> Optional[Decimal]:
        pass

    @abstractmethod
    def source_name(self):
        pass
