import abc


class IntentClassifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract_intent(self, query: str):
        pass

class IntentClassifierImpl(IntentClassifier):
    def __init__(self, model):
        self._model = model

    def extract_intent(self, query: str):
        pass