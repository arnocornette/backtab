from price import Price
from typing import Optional


class Product:
    name: str
    currency: str
    price: Price
    image: str
    category: Optional[str]
    visible: Optional[bool]
