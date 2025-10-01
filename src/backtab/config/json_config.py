from typing import override
from backtab.config.loader import ConfigLoader
from backtab.logger import log

from backtab.model.config import Config


class JsonConfig(ConfigLoader):
    @override
    @staticmethod
    def load(path: str) -> Config:
        try:
            with open(path, "r") as config_file:
                config = config_file.read()
                return Config.model_validate_json(config)
        except FileNotFoundError:
            log.error("Error loading config file")
            # TODO: Add correcy exception
            raise Exception()
