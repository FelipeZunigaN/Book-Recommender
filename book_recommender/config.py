import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = "data/books_with_emotions.csv"
EMBEDDINGS_FILE = "embeddings/tagged_description.txt"
PERSIST_DIR = "chroma_db_books"
