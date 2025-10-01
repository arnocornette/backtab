import contextlib
import threading

repo_lock = threading.RLock()


@contextlib.contextmanager
def transaction():
    """Get the repo lock. Designed to be used with a with statement"""
    with repo_lock:
        yield
