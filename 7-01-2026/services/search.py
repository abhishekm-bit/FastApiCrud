from services.embedding import generate_embedding
from services.vector_store import get_collection

def search_similar(query: str):
    collection = get_collection()
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    return results
