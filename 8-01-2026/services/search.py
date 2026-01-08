from services.embedding import generate_embedding
from services.vector_store import get_collection

def store_chunks(chunks):
    collection = get_collection()

    for i, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)
        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk]
        )

def search_chunks(query, top_k):
    collection = get_collection()
    query_embedding = generate_embedding(query)

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "embeddings", "distances"]  # 👈 important
    )

    return result
