import chromadb

# create db client
client = chromadb.Client()

def get_collection():
    """
    Returns ChromaDB collection
    """
    return client.get_or_create_collection(name="queries")
