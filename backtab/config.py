import os.path
from json import JSONDecodeError, load
from backtab.logger import log

required_keys = ["data", "host", "port", "remote_url", "clone_url"]
config_file = os.getenv("CONFIG_FILE", "config.json")


class BacktabConfig:
    DATA_DIR: str = os.path.join(os.getcwd(), "../data/mut_data")
    LISTEN_ADDR: str = "localhost"
    SLOWDOWN: float = 0.1
    EVENT_MODE: bool = False
    data: str = ""
    host: str = "localhost"
    port: int = 8000
    remote_url: str = ""
    clone_url: str = ""

    def __init__(
        self, data_path: str, host: str, port: int, remote_url: str, clone_url: str
    ) -> None:
        self.data = os.path.join(os.getcwd(), data_path)
        self.host = host
        self.port = port
        self.remote_url = remote_url
        self.clone_url = clone_url


def load_from_config(configPath: str) -> BacktabConfig:
    try:
        with open(configPath) as file:
            config: dict[str, str] = load(file)  # pyright: ignore[reportAny]
            return BacktabConfig(
                config["data"],
                config["host"],
                int(config["port"]),
                config["remote_url"],
                config["clone_url"],
            )
    except JSONDecodeError as json_error:
        log.error(f"Error decoding/loading BacktabConfig file {json_error}")
        raise Exception()


APP_CONFIG = load_from_config(config_file)
SERVER_CONFIG = load_from_config(config_file)
