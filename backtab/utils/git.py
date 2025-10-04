import contextlib
from git import GitCommandError, Repo
from backtab.config import APP_CONFIG
from backtab.logger import log
from pathlib import Path

initial_folders = ["products", "members"]
initial_structure: dict[str, list[str]] = {
    "products": [],
    "members": [],
}


def setup_initial_data(path: str):
    log.info("Setup initial data structure")
    for folder_key in initial_structure:
        Path(f"{path}/{folder_key}").mkdir(parents=True, exist_ok=True)
        for file in initial_structure[folder_key]:
            with open(f"{path}/{folder_key}/{file}", "w+"):
                pass


def get_or_create_repo(path: str):
    try:
        print(path)
        if Path(path).exists():
            log.info(f"Using existing Repo: {path}")
            return Repo(path)
        Path(path).mkdir(exist_ok=True)
        log.info(f"Cloning from {APP_CONFIG.clone_url}")
        repo = Repo.clone_from(url=APP_CONFIG.clone_url, to_path=path)
        setup_initial_data(path)
        return repo
    except GitCommandError as e:
        print(e)
        repo = Repo.init(APP_CONFIG.data)
        remotes = repo.remotes
        if "origin" not in remotes:
            log.info(f"Creating new remote test with url {APP_CONFIG.remote_url}")
            _ = repo.create_remote("test", APP_CONFIG.remote_url)
        setup_initial_data(path)
        log.info("Created and setup data directory")
        return repo


repo = get_or_create_repo(APP_CONFIG.data)


def pull_data():
    log.info("Pulling changes")
    _ = repo.remotes.origin.pull()


def push():
    log.info("Pushing changes")
    _ = repo.remotes.origin.push()


@contextlib.contextmanager
def commit(transaction: str):
    try:
        yield
        _ = repo.commit(transaction)
    except GitCommandError:
        log.error("Could not commit transaction")
        _ = repo.head.reset(index=True, working_tree=True)
