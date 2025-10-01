import typing
from backtab.model.member import Member
from backtab.model.product import Product


class BacktabRepo:
    members: typing.Dict[str, Member]
    products: typing.Dict[str, Product]
