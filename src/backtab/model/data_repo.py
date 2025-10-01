from abc import ABC, abstractmethod


class DataRepository(ABC):
    @abstractmethod
    def pull(self):
        pass

    @abstractmethod
    def pull_accounts(self):
        pass

    @abstractmethod
    def pull_products(self):
        pass

    @abstractmethod
    def type():
        pass

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def push_products(self):
        pass

    @abstractmethod
    def push_accounts(self):
        pass
