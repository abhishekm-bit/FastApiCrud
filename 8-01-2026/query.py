from cosine_similarity import search_chunks_cosine

query = "W"
results = search_chunks_cosine(query, top_k=3)

print("\n✅ Top matching chunks:\n")

for i, item in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print("Score:", round(item["score"], 3))
    print("Text:")
    print(item["document"].strip())
    print()
