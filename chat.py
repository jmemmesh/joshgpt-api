import abc


class Chat(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def respond(self, query: str):
        pass

class ChatImpl(Chat):
    def __init__(self, intent_classifier, metadata_extractor, retriever, llm):
        self._intent_classifier = intent_classifier
        self._metadata_extractor = metadata_extractor
        self._retriever = retriever
        self._llm = llm

    def respond(self, query: str):
        #metadata = self._metadata_extractor.extract_metadata(query)
        #docs = self._retriever.search(metadata)
        docs = "5 years of experience in Kafka. 10 years of experience in Java"
        response = self._llm.answer(query, docs)
        return response