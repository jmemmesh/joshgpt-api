import abc
from transformers import pipeline

class LLM(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def answer(self, query, context):
        pass

class LLMImpl(LLM):
    def __init__(self, model_name):
        self._model_name = model_name
        self._nlp = pipeline("text-generation", model=self._model_name, max_length=200)

    def answer(self, query, context):
        content = f"Query: {query} Context: {context}"
        messages = [
            {"role": "system", "content": "You answer questions on a resume, responding like you are that person."},
            {"role": "system", "content": f"Here is the resume: {context}"},
            {"role": "user", "content": query},
        ]

        print(self._nlp(messages))