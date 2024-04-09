import datetime
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CurrencyStatusDTO:
    currency: str
    value: Decimal
    dt: datetime.datetime
    source: str



