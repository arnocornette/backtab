from beancount.core.inventory import Inventory
from backtab.accounts.account import BacktabAccount


class BacktabRepo:
    accounts: dict[str, BacktabAccount]
    products: dict[str, str]
    instance_ledger_uncommitted: bool = True

    def __init__(self) -> None:
        self.accounts = {"str": BacktabAccount("test", "test", 123, Inventory())}
        self.products = {"str": "str"}
