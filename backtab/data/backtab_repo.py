from typing import Any, final

from backtab.config import APP_CONFIG
from os import listdir
from backtab.members.member import BacktabMember
from backtab.members.members_loader import BacktabMembersLoader
from backtab.products.product import BacktabProduct
from backtab.products.products_loader import BacktabProductsLoader
from backtab.logger import log
from backtab.utils.git import commit
from backtab.utils.transaction import add_product


@final
class BacktabDataRepo:
    products: list[BacktabProduct]
    members: list[BacktabMember]
    entries: Any
    product_path = f"{APP_CONFIG.data}/products"
    member_path = f"{APP_CONFIG.data}/members"

    def __init__(self):
        self.products = self.parse_products_from_repo()
        self.members = self.parse_members_from_repo()
        self.entries = []

    def parse_products_from_repo(self) -> list[BacktabProduct]:
        products_list = listdir(self.product_path)
        result: list[BacktabProduct] = []
        for path in products_list:
            with open(f"{self.product_path}/{path}") as detail:
                product = BacktabProductsLoader.load_from_json(detail.read())
                result.append(product)
        log.info(f"Loaded {len(result)} products")
        return result

    # TODO: should we look into optimizing the reading of files?
    def parse_members_from_repo(self) -> list[BacktabMember]:
        members_list = listdir(self.member_path)
        result: list[BacktabMember] = []
        for path in members_list:
            with open(f"{self.member_path}/{path}") as detail:
                member = BacktabMembersLoader.load_from_json(detail.read())
                result.append(member)

        log.info(f"Loaded {len(result)} members")
        return result

    def add_product(self, product: BacktabProduct):
        product_name = product.name.replace(" ", "_").lower()
        with open(f"{self.product_path}/{product_name}.json", "w+") as product_file:
            _ = product_file.write(str(product))
            _ = commit(add_product)

    def add_member(self, member: BacktabMember):
        with open(f"{self.member_path}/{member.name}.json", "w+") as member_file:
            _ = member_file.write(str(member))
            _ = commit(add_product)


backtab_repo = BacktabDataRepo()
