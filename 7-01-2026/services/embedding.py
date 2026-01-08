import ollama
from config import EMBEDDING_MODEL
# Embedding
def generate_embedding(text: str):
    response = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=text
    )
    return response["embedding"]
