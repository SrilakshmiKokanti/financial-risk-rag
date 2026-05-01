from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from rag.loader import load_documents
from rag.indexer import load_index

def get_hybrid_retriever(k=5):
    docs = load_documents()
    bm25 = BM25Retriever.from_documents(docs)
    bm25.k = k
    faiss_ret = load_index().as_retriever(search_kwargs={'k': k})
    return EnsembleRetriever(retrievers=[bm25, faiss_ret], weights=[0.4, 0.6])