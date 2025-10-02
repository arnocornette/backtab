from backtab.config.util import backtab_config
from backtab.server import api
from backtab.data_repo import REPO_DATA
import time


@api.get("/accounts")
def accounts():
    time.sleep(backtab_config.slowdown)
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
