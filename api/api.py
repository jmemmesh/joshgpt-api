from fastapi import APIRouter, Request, Depends
from chat import ChatImpl

router = APIRouter()

def get_intent_classifier(request: Request):
    return request.state.intent_classifier

def get_metadata_extractor(request: Request):
    return request.state.metadata_extractor

def get_retriever(request: Request):
    return request.state.retriever

def get_LLM(request: Request):
    return request.state.llm

@router.get("/get_answer")
def get_answer(query: str,
               llm = Depends(get_LLM),
               retriever = Depends(get_retriever),
               intent_classifier = Depends(get_intent_classifier),
               metadata_extractor = Depends(get_metadata_extractor)):
    chat = ChatImpl(intent_classifier=intent_classifier,
                    metadata_extractor=metadata_extractor,
                    retriever=retriever,
                    llm=llm)
    response = chat.respond(query)
    return {"query": query,
            "answer": response}