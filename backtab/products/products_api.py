# endpoints
# get_all
# get
# add

from backtab.data.backtab_repo import backtab_repo
from fastapi import APIRouter

from backtab.products.product import BacktabProduct

products_router = APIRouter()


# Get all products
@products_router.get("/products")
def products():
    return backtab_repo.products


@products_router.get("/products/{product_ean}")
def product(product_ean: str) -> BacktabProduct:
    return next(filter(lambda p: p.ean == int(product_ean), backtab_repo.products))


@products_router.post("/products")
def add(product: BacktabProduct):
    backtab_repo.add_product(product)
    pass
