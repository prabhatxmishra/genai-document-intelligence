from fastapi import FastAPI
from pydantic import BaseModel
from app.llm import call_hf_llm

app = FastAPI(title="GenAI Chat Service (Hugging Face)")


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    question: str
    answer: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # You can add system prompt / formatting here
    prompt = f"User question: {req.question}\nAnswer clearly:"
    answer = call_hf_llm(prompt)
    return ChatResponse(question=req.question, answer=answer)
