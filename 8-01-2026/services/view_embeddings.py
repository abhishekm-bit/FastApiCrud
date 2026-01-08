from vector_store import get_collection

collection = get_collection()

# Ask ChromaDB to include embeddings
results = collection.get(
    include=["documents", "embeddings"]
)

documents = results["documents"]
embeddings = results["embeddings"]

print("\n--- CHUNKS WITH EMBEDDINGS ---\n")

for i, (doc, emb) in enumerate(zip(documents, embeddings), start=1):
    print(f"--- Chunk {i} ---")
    print("Text:")
    print(doc[:200], "...")   # print first 200 chars only
    print("\nEmbedding length:", len(emb))
    print("Embedding (first 10 values):")
    print(emb[:10])
    print("-" * 60)
