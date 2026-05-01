from langchain.tools import tool
from rag.retriever import get_hybrid_retriever

retriever = get_hybrid_retriever()

@tool
def search_financial_docs(query: str) -> str:
    '''Search financial policy and risk documents.'''
    docs = retriever.invoke(query)
    if not docs:
        return 'No relevant documents found.'
    out = []
    for i, doc in enumerate(docs):
        src = doc.metadata.get('source', 'unknown')
        out.append(f'[{i+1}] Source: {src}\n{doc.page_content}')
    return '\n\n'.join(out)

@tool
def calculate_risk_score(probability: float, impact: float) -> str:
    '''Calculate risk score from probability (0-1) and impact (0-10).'''
    score = probability * impact
    level = 'LOW' if score < 2 else 'MEDIUM' if score < 5 else 'HIGH' if score < 8 else 'CRITICAL'
    return f'Risk Score: {score:.2f} - Level: {level}'