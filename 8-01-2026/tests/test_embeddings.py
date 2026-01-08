from services.embedding import generate_embedding
def test_embedding_returns_vector():
    embedding = generate_embedding("What is Machine Learning?")
    
    assert embedding is not None
    assert isinstance(embedding, list)
    assert len(embedding) > 0


def test_embedding_is_numeric():
    embedding = generate_embedding("Neural Networks")
    
    assert all(isinstance(x, (int, float)) for x in embedding)
