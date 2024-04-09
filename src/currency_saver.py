from abc import ABC, abstractmethod


class CurrencySaver(ABC):
    @abstractmethod
    def save(self, CurrencyStatusDTO):
        pass
