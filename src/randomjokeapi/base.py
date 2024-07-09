from abc import ABC, abstractmethod


class Joke(ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def get_random_joke(self):
        pass