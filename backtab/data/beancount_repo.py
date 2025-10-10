from typing import Any, final
from beancount.api import Directives, Options
from beancount.loader import load_file
from backtab import config


@final
class BeancountRepo:
    beancount_file = f"{config.APP_CONFIG.DATA_DIR}/kolab.beancount"
    repo: tuple[Directives, list[Any], list[Options]]

    def __init__(self) -> None:
        self.repo = load_file(self.beancount_file)
        pass

    pass
