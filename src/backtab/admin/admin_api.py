# Admin
#
from backtab.server import api
from backtab.config.util import backtab_config
from backtab.data_repo import REPO_DATA, UpdateFailed
import time


@api.get("/admin/update")
def update():
    time.sleep(backtab_config.slowdown)
    try:
        REPO_DATA.pull_changes()
        return "Success"
    except UpdateFailed:
        raise Exception()
