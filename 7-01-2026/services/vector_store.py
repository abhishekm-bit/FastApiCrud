import chromadb
from config import COLLECTION_NAME

client = chromadb.Client()

def get_collection():
    return client.get_or_create_collection(name=COLLECTION_NAME)
