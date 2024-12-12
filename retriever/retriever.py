import abc
from typing import Dict, List

class Retriever(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def search(self, metadata: Dict[str, List[str]]):
        pass

class RetrieverImpl(Retriever):
    def __init__(self):
        pass

    def search(self, metadata: Dict[str, List[str]]):
        pass
