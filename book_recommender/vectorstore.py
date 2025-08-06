import os
import logging
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from .config import EMBEDDINGS_FILE, PERSIST_DIR

embedding_model = OpenAIEmbeddings()

def get_vectorstore():
    if os.path.exists(PERSIST_DIR):
        logging.info("✅ Loading existing Chroma DB")
        return Chroma(persist_directory=PERSIST_DIR, embedding_function=embedding_model)

    logging.info("📄 Loading and splitting documents...")
    raw_doc = TextLoader(EMBEDDINGS_FILE, encoding="utf-8").load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0, separator="\n")
    docs = splitter.split_documents(raw_doc)

    logging.info("🧠 Generating embeddings and saving Chroma DB")
    db = Chroma.from_documents(docs, embedding=embedding_model, persist_directory=PERSIST_DIR)
    db.persist()
    return db
