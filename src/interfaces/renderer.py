from abc import ABC, abstractmethod


class IRenderer(ABC):

    @abstractmethod
    def draw(self, frame_data):
        pass