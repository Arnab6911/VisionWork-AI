from abc import ABC, abstractmethod


class IManager(ABC):

    @abstractmethod
    def update(self, tracks):
        pass