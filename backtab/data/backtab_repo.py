from backtab.config import APP_CONFIG
from pathlib import Path
from os import listdir
from backtab.members.member import BacktabMember
from backtab.members.members_loader import BacktabMembersLoader
from backtab.products.product import BacktabProduct
from backtab.products.products_loader import BacktabProductsLoader


class BacktabDataRepo:
    products: dict[str, BacktabProduct]
    members: dict[str, BacktabMember]

    def __init__(self):
        self.products = self.parse_products()
        self.members = self.parse_members()

    # account: dict[str, Account]
    def parse_products(self):
        product_path = f"{APP_CONFIG.data}/products"
        products_list = listdir(product_path)
        result: dict[str, BacktabProduct] = {}
        for path in products_list:
            with open(f"{product_path}/{path}") as detail:
                product = BacktabProductsLoader.load_from_json(detail.read())
                print(product.ean)
                result["" + product.ean] = product
        return result

    def parse_members(self):
        member_path = f"{APP_CONFIG.data}/members"
        members_list = listdir(member_path)
        result: dict[str, BacktabMember] = []  # pyright: ignore[reportAssignmentType]
        for path in members_list:
            with open(f"{member_path}/{path}") as detail:
                member = BacktabMembersLoader.load_from_json(detail.read())
                result[member.account_name] = member
        return result


backtab_repo = BacktabDataRepo()
