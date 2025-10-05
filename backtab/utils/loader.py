from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    def load(raw_data):
        pass
