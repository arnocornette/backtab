from dataclasses import dataclass
from beancount.core.inventory import Inventory


@dataclass
class BacktabMember:
    account_name: str
    id: int
    display_name: str
    pin: int
    inventory: Inventory
    is_member: bool = False
