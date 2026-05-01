import re
from langchain_core.messages import HumanMessage, SystemMessage
from app.config import get_llm
from rag.retriever import get_hybrid_retriever
from agent.prompts import SYSTEM_PROMPT

async def run_agent(query: str, session_id: str) -> dict:
    llm = get_llm()
    retriever = get_hybrid_retriever()

    docs = retriever.invoke(query)
    context = "\n\n".join([
        f"[Source: {doc.metadata.get('source', 'unknown')}]\n{doc.page_content}"
        for doc in docs
    ])

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Context:\n{context}\n\nQuestion: {query}")
    ]

    response = await llm.ainvoke(messages)
    answer = response.content

    sources = list(set([
        doc.metadata.get("source", "unknown") for doc in docs
    ]))

    return {"answer": answer, "sources": sources}