from db.vector_db import store_vectors, search
from services.embeddings import embed

def test_vector_search():
    texts = ["python", "java", "react"]
    vectors = embed(texts)

    store_vectors(vectors, texts)

    q_vec = embed(["python"])
    result = search(q_vec)

    assert "python" in result
