from beancount.core.inventory import Inventory


class BacktabAccount:
    account_name: str
    display_name: str
    pin: int
    inventory: Inventory
    # TODO: Should we assume that we only create this object when we find the user file in the repo
    is_member: bool

    def __init__(
        self,
        account_name: str,
        display_name: str,
        pin: int,
        inventory: Inventory,
        is_member: bool = True,
    ) -> None:
        self.account_name = account_name
        self.display_name = display_name
        self.pin = pin
        self.inventory = inventory
        self.is_member = is_member
