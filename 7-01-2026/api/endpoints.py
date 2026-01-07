from services.search import search_similar

def search_endpoint(query: str):
    """
    Simple API-like function
    """
    result = search_similar(query)
    return result
