from pathlib import Path
from backtab.logger import log

initial_folders = ["products", "accounts"]
# Add str in the list to have them created as empty files
initial_structure: dict[str, list[str]] = {
    "products": [],
    "accounts": [],
}


def setup_initial_data(path: str):
    log.info("Setup initial data structure")
    for folder_key in initial_structure:
        Path(f"{path}/{folder_key}").mkdir(parents=True, exist_ok=True)
        for file in initial_structure[folder_key]:
            with open(f"{path}/{folder_key}/{file}", "w+") as f:
                pass
