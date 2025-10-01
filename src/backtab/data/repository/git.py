from typing import override
from backtab.model.data_repo import DataRepository
from git import Repo
from backtab.config.config_util import ConfigData

class GitRepo(DataRepository):
    def __init__(self) -> None:
        super().__init__()
        # Check if the repo exists locally
        # otherwise pull repo
        Repo.clone_from(config.)

    @override
    def pull(self):
        pass

    @override
    def pull_products(self):
        pass

    @override
    def pull_accounts(self):
        pass

    @override
    def push(self):
        pass

    @override
    def push_products(self):
        pass

    @override
    def push_accounts(self):
        pass

    @override
    def type():
        "git"
