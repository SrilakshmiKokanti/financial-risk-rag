from fastapi import APIRouter
from pydantic import BaseModel
from agent.graph import run_agent
import time

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    session_id: str = 'default'

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    latency_ms: float

@router.post('/chat', response_model=ChatResponse)
async def chat(req: ChatRequest):
    start = time.time()
    result = await run_agent(req.query, req.session_id)
    latency = (time.time() - start) * 1000
    return ChatResponse(answer=result['answer'], sources=result['sources'], latency_ms=round(latency, 2))