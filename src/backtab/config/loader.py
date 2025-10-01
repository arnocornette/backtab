from abc import ABC, abstractmethod
from backtab.model.config import Config


class ConfigLoader(ABC):
    @abstractmethod
    @staticmethod
    def load(path: str) -> Config:
        pass
