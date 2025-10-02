# endpoints
# get_all
# get
# add

from bottle import Bottle, get
from backtab.config import SERVER_CONFIG
import time

products_api = Bottle()


@get("/products")
def products():
    time.sleep(SERVER_CONFIG.SLOWDOWN)
    return {
        name: product.to_json()
        for name, product in filter(
            lambda item: item[1].visible, REPO_DATA.products.items()
        )
    }
