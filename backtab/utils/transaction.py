import contextlib
from dataclasses import dataclass
import threading


repo_lock = threading.RLock()


@dataclass
class BacktabDataUpdate:
    action: str
    group: str
    message: str


class BacktabTransaction:
    pass


add_product = BacktabDataUpdate("add", "product", "added new product")
pull_data = BacktabDataUpdate("pull", "general", "pull new data")
push_data = BacktabDataUpdate("push", "general", "push new data")


@contextlib.contextmanager
def transaction():
    """Get the repo lock. Designed to be used with a with statement"""
    with repo_lock:
        yield
