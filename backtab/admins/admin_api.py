# Admin
#
from backtab.server import api
from backtab.data_repo import UpdateFailed
from backtab.utils.git import get_or_pull_repo


@api.get("/admin/update")
def update():
    try:
        return get_or_pull_repo()
    except UpdateFailed:
        raise Exception()
