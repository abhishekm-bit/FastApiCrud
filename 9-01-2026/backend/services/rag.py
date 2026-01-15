from db.vector_db import search

def retrieve(query_vector):
    return search(query_vector)
