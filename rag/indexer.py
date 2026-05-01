import os
from langchain_community.vectorstores import FAISS
from rag.loader import load_documents
from rag.embedder import get_embedder
from app.config import FAISS_INDEX_PATH

def build_index():
    docs = load_documents()
    db = FAISS.from_documents(docs, get_embedder())
    os.makedirs(FAISS_INDEX_PATH, exist_ok=True)
    db.save_local(FAISS_INDEX_PATH)
    print(f'Index built with {len(docs)} chunks.')
    return db

def load_index():
    return FAISS.load_local(FAISS_INDEX_PATH, get_embedder(), allow_dangerous_deserialization=True)