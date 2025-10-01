from pydantic import BaseModel
from backtab.model.price import Price


class Product(BaseModel):
    name: str
    currency: str
    price: Price
    image: str
    category: str | None
    visible: bool = True
