from git import Repo
from os import getenv

git_url = getenv("GIT_REPO")
repo = Repo(git_url)


def get_or_pull_repo():
    return repo.remotes.origin.pull()


def push_repo(force: bool = False):
    repo.remotes.origin.push()
    pass
