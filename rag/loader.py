import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import DOCS_PATH

def load_documents():
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
    for fname in os.listdir(DOCS_PATH):
        fpath = os.path.join(DOCS_PATH, fname)
        if fname.endswith('.pdf'):
            loader = PyPDFLoader(fpath)
        elif fname.endswith('.txt'):
            loader = TextLoader(fpath)
        else:
            continue
        docs.extend(splitter.split_documents(loader.load()))
    return docs