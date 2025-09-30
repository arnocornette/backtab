# Admin
#
from bottle import get
from backtab.config import backtab_config
import time


@get("/admin/update")
def update():
    time.sleep(backtab_config.slowdown)
    try:
        REPO_DATA.pull_changes()
        return "Success"
    except UpdateFailed:
        raise bottle.HTTPResponse(body=traceback.format_exc())
