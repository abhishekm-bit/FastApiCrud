from cosine_similarity import search_chunks_cosine

def test_top_k_limit():
    results = search_chunks_cosine("AI", top_k=2)
    assert len(results) <= 2
