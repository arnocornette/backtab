from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class BacktabProductPrice(JSONWizard):
    member: float
    guest: float


@dataclass
class BacktabProduct(JSONWizard):
    product_name: str
    product_price: BacktabProductPrice
    image: str | None
    ean: str
