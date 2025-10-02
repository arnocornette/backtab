# endpoints
# get_all
# get
# add

from bottle import Bottle
from backtab.config import SERVER_CONFIG
from backtab.data_repo import REPO_DATA
import time


@products_api.get("/products")
def products():
    time.sleep(SERVER_CONFIG.SLOWDOWN)
    return {
        name: product.to_json()
        for name, product in filter(
            lambda item: item[1].visible, REPO_DATA.products.items()
        )
    }
