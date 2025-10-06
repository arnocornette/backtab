# Admin
#
from fastapi import APIRouter

from backtab.utils.git import pull_data, push_data

admin_router = APIRouter()


class HttpStatus:
    status: str

    def __init__(self, status: str) -> None:
        self.status = status


@admin_router.get("/admin/pull")
def update():
    pull_data()
    return HttpStatus("OK")


@admin_router.get("/admin/push")
def push():
    push_data()
    return HttpStatus("OK")
