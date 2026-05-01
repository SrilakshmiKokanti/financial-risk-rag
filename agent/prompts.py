from langchain.prompts import ChatPromptTemplate

SYSTEM_PROMPT = (
    'You are a financial risk expert assistant. '
    'Answer questions strictly based on the provided context from financial documents. '
    'If the answer is not in the context, say you do not have enough information. '
    'Always cite the source document. Be concise and professional.'
)

RAG_PROMPT = ChatPromptTemplate.from_messages([
    ('system', SYSTEM_PROMPT),
    ('human', 'Context:\n{context}\n\nQuestion: {question}\n\nAnswer based only on the context.'),
])