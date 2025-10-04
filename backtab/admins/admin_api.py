# Admin
#
from fastapi import APIRouter

admin_router = APIRouter()


@admin_router.get("/admin/update")
def update():
    pass


@admin_router.get("/admin/push")
def push():
    return f""
