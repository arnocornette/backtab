from git import GitCommandError, Repo
from os import getenv
import contextlib
from backtab.logger import log
from backtab.utils.repo import setup_initial_data

DATA_PATH = getenv("DATA_PATH", "./test")
git_url = "git@github.com:arnocornette/tab-data"


def setup_repo_folder(path: str):
    try:
        return Repo.clone_from(url=git_url, to_path=path)
    except GitCommandError as git_error:
        repo = Repo.init(DATA_PATH)
        remotes = repo.remotes
        if "test" not in remotes:
            log.info(f"Creating new remote test with url {git_url}")
            _ = repo.create_remote("test", git_url)

        setup_initial_data(path)
        return repo


repo = setup_repo_folder("./test")


def get_or_pull_repo():
    return repo.remotes.origin.pull()


def push_repo(force: bool = False):
    return repo.remotes.test.push()


# TODO: Switch transacation to a Transaction object
@contextlib.contextmanager
def git_transaction(self, transaction: str):
    head = repo.head
    try:
        yield
        repo.commit(transaction)
    except Exception:
        value = repo.head.reset(index=True, working_tree=True)

    self.synchronized = False
