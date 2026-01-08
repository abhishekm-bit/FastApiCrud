import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from services.embedding import generate_embedding
from services.vector_store import get_collection


def search_chunks_cosine(query, top_k):
    collection = get_collection()

    # get ALL stored data
    data = collection.get(include=["documents", "embeddings"])

    if data["embeddings"] is None or not np.any(data["embeddings"]):
        return []

    query_embedding = generate_embedding(query)

    # convert to numpy
    db_embeddings = np.array(data["embeddings"])
    query_embedding = np.array(query_embedding).reshape(1, -1)

    # cosine similarity (0 → 1)
    scores = cosine_similarity(query_embedding, db_embeddings)[0]

    # get top K highest
    top_indices = scores.argsort()[-top_k:][::-1]

    results = []
    for idx in top_indices:
        results.append({
            # 🔥 scale similarity to 0 → 10
            "score": round(float(scores[idx] * 10), 2),
            "document": data["documents"][idx]
        })

    return results
