from services.embeddings import embed

def test_embedding_shape():
    texts = ["hello world", "machine learning"]
    vectors = embed(texts)

    assert len(vectors) == 2
    assert len(vectors[0]) == 384  # dimension
