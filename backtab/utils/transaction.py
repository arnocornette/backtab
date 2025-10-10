import contextlib
from dataclasses import dataclass
from functools import wraps
import threading
from typing import Callable
from backtab.members.member import BacktabMember
from beancount.core.data import Transaction
from datetime import datetime

repo_lock = threading.RLock()


@dataclass
class BacktabDataUpdate:
    action: str
    group: str
    message: str


class BacktabTransaction:
    primary_account: BacktabMember | None

    def __init__(
        self,
        title: str | None,
        date: datetime | None = None,
        meta: dict[str, str] | None = None,
    ):
        if meta is None:
            meta = {}
        if date is None:
            date = datetime.now()
        if title is None:
            raise TypeError("Title must be provided for a transaction")
        self.txn = Transaction(
            meta,
            date,
            flag="txn",
            payee=None,
            narration=title,
            tags=set(),
            links=set(),
            postings=[],
        )
        self.primary_account = None


add_product = BacktabDataUpdate("add", "product", "added new product")
pull_data = BacktabDataUpdate("pull", "general", "pull new data")
push_data = BacktabDataUpdate("push", "general", "push new data")


@contextlib.contextmanager
def transaction():
    """Get the repo lock. Designed to be used with a with statement"""
    with repo_lock:
        yield


def json_txt_method(transaction: BacktabTransaction):
    def apply_json_txn_method(fn: Callable[..., BacktabTransaction]):
        @wraps(fn)
        def result():
            txn = fn(transaction)
            return txn
