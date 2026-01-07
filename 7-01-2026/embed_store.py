import chromadb
import ollama

# connect to chromadb
client = chromadb.Client()

# create or get collection (table)
collection = client.get_or_create_collection(name="queries")

# text to embed
text = "Can I know policy of Cascade Clouds?"
# generate embedding using ollama
response = ollama.embeddings(
    model="nomic-embed-text",
    prompt=text
)
embedding = response["embedding"]

# store in vector database
collection.add(
    ids=["query1"],
    embeddings=[embedding],
    documents=[text]
)

print("Completed Query embedded and Store into ChromaDb")
