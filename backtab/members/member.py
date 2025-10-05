from dataclasses import dataclass
from beancount.core.inventory import Inventory


@dataclass
class BacktabMember:
    name: str
    id: int
    display: str
    pin: str
    inventory: Inventory
    # assuming only members have member definition
    is_member: bool = False
