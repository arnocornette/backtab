from backtab.admins.admin_api import admin_router
from backtab.data_repo import REPO_DATA
from fastapi import FastAPI

from backtab.products.products_api import products_router
from backtab.utils.git import pull_data

api = FastAPI()
api.include_router(admin_router)
api.include_router(products_router)
# def json_txn_method(fn: typing.Callable[[typing.Dict], data_repo.Transaction]):
#     @wraps(fn)
#     def result():
#         member_deltas = REPO_DATA.apply_txn(txn)
#         return {
#             "members": {
#                 member.internal_name: {
#                     "balance": str(-member.balance_eur),
#                     "items": member.item_count,
#                 }
#                 for member in member_deltas
#             },
#             "message": txn.beancount_txn.narration
#             + (
#                 " (and now has €%s)" % (-txn.primary_account.balance_eur,)
#                 if txn.primary_account is not None
#                 else ""
#             ),
#         }
#
#     return result


# @api.post("/txn/deposit")
# @json_txn_method
# def deposit(json):
#     return data_repo.DepositTxn(
#         member=REPO_DATA.accounts[json["member"]],
#         amount=decimal.Decimal(json["amount"]),
#     )
#
#
# @api.post("/txn/xfer")
# @json_txn_method
# def transfer(json):
#     return data_repo.TransferTxn(
#         payer=REPO_DATA.accounts[json["payer"]],
#         payee=REPO_DATA.accounts[json["payee"]],
#         amount=decimal.Decimal(json["amount"]),
#     )
#
#
# @api.post("/txn/buy")
# @json_txn_method
# def buy(json):
#     return data_repo.BuyTxn(
#         buyer=REPO_DATA.accounts[json["member"]],
#         products=[
#             (REPO_DATA.products[product], count)
#             for product, count in json["products"].items()
#         ],
#     )
#


def main():
    # Load config
    pull_data()
    REPO_DATA.pull_changes()


if __name__ == "__main__":
    main()
