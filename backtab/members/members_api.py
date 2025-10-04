from backtab.server import api
from backtab.data_repo import REPO_DATA


@api.get("/members")
def accounts():
    return {
        name: {
            "display_name": member.display_name,
            # The balance is negative in the ledger, because the
            # accounts are seen from the hackerspace's viewpoint
            "balance": str(-member.balance_eur),
            "items": member.item_count,
        }
        for name, member in REPO_DATA.accounts.items()
    }


@api.get("/members/<account_name>")
def get_account(account_name: str):
    # TODO: Implement functionality
    return f"Not implemented {account_name}"
