from contextlib import asynccontextmanager
from intent.intent import IntentClassifierImpl
from llm.llm import LLMImpl
from retriever.retriever import RetrieverImpl
from metadata.metadata import MetadataExtractorImpl


@asynccontextmanager
async def lifespan(app):
    intent_classifier = IntentClassifierImpl(
        model="TODO"
    )
    metadata_extractor = MetadataExtractorImpl()
    retriever = RetrieverImpl()
    llm = LLMImpl(
        model_name="Qwen/Qwen2.5-1.5B-Instruct"
    )
    try:
        yield {
            "intent_classifier": intent_classifier,
            "metadata_extractor": metadata_extractor,
            "llm": llm,
            "retriever": retriever
        }
    finally:
        pass