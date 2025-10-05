# Admin
#
from fastapi import APIRouter

from backtab.utils.git import pull_data, push_data

admin_router = APIRouter()


@admin_router.get("/admin/pull")
def update():
    pull_data()
    pass


@admin_router.get("/admin/push")
def push():
    push_data()
    return f""
