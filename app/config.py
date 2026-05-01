import os
from dotenv import load_dotenv
load_dotenv()

LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'groq').lower()
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama3-8b-8192')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
ANTHROPIC_MODEL = os.getenv('ANTHROPIC_MODEL', 'claude-3-5-sonnet-20241022')
FAISS_INDEX_PATH = os.getenv('FAISS_INDEX_PATH', './faiss_index')
DOCS_PATH = os.getenv('DOCS_PATH', './docs')

def get_llm():
    if LLM_PROVIDER == 'anthropic':
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model=ANTHROPIC_MODEL, anthropic_api_key=ANTHROPIC_API_KEY, temperature=0)
    if LLM_PROVIDER == 'groq':
        from langchain_groq import ChatGroq
        return ChatGroq(model=GROQ_MODEL, groq_api_key=GROQ_API_KEY, temperature=0)
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(model=OPENAI_MODEL, openai_api_key=OPENAI_API_KEY, temperature=0)

def get_embeddings():
    from langchain_huggingface import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')