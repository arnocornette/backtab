# endpoints
# get_all
# get
# add

from backtab.data_repo import REPO_DATA
from backtab.server import api


@api.get("/products")
def products():
    return {
        name: product.to_json()
        for name, product in filter(
            lambda item: item[1].visible, REPO_DATA.products.items()
        )
    }
