import contextlib
from dataclasses import dataclass
from enum import StrEnum
import threading


repo_lock = threading.RLock()


class BacktabTransactionAction(StrEnum):
    ADD_PRODUCT = "ADD_PRODUCT"
    PUSH = "PUSH"
    PULL = "PULL"


@contextlib.contextmanager
def transaction():
    """Get the repo lock. Designed to be used with a with statement"""
    with repo_lock:
        yield


@dataclass
class BacktabTransaction:
    action: str
    group: str
    message: str


add_product = BacktabTransaction("add", "product", "added new product")
pull_data = BacktabTransaction("pull", "general", "pull new data")
push_data = BacktabTransaction("push", "general", "push new data")
