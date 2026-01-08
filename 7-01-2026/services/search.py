from services.embedding import generate_embedding
from services.vector_store import get_collection

def store_text(text: str, doc_id: str):
    collection = get_collection()
    embedding = generate_embedding(text)

    collection.add(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text]
    )

def search_text(query: str):
    collection = get_collection()
    query_embedding = generate_embedding(query)

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )
    return result
