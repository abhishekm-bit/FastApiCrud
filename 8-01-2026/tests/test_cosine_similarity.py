import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def test_identical_vectors_have_high_similarity():
    v1 = np.array([[1, 1]])
    v2 = np.array([[1, 1]])

    score = cosine_similarity(v1, v2)[0][0]
    assert round(score, 3) == 1.0


def test_opposite_vectors_have_low_similarity():
    v1 = np.array([[1, 1]])
    v2 = np.array([[-1, -1]])

    score = cosine_similarity(v1, v2)[0][0]
    assert score < 0


def test_unrelated_vectors_have_low_similarity():
    v1 = np.array([[1, 0]])
    v2 = np.array([[0, 1]])

    score = cosine_similarity(v1, v2)[0][0]
    assert round(score, 3) == 0.0
