from fastapi import FastAPI
from app.routes import chat, ingest

app = FastAPI(
    title='Financial Risk RAG Assistant',
    description='Domain-focused GenAI assistant over financial risk documents.',
    version='1.0.0',
)
app.include_router(chat.router)
app.include_router(ingest.router)

@app.get('/health')
def health():
    return {'status': 'ok'}