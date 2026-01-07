import ollama

def generate_embedding(text: str):
    """
    Converts text into vector embedding
    """
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]
