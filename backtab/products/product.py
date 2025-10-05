from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class BacktabProductPrice(JSONWizard):
    member: float
    guest: float


@dataclass
class BacktabProduct(JSONWizard):
    name: str
    ean: int
    price: BacktabProductPrice
    image: str | None = ""
