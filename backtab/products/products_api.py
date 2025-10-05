# endpoints
# get_all
# get
# add

from backtab.data.backtab_repo import backtab_repo
from fastapi import APIRouter

products_router = APIRouter()


@products_router.get("/products")
def products():
    return backtab_repo.products
