from cosine_similarity import search_chunks_cosine

query = "What is the FeedForward Neural Network I wanted More Explanation"
results = search_chunks_cosine(query, top_k=15)

# 🔥 Ensure results are sorted by highest cosine similarity
results = sorted(results, key=lambda x: x["score"], reverse=True)

print("\n✅ Top highest matching chunks:\n")

for i, item in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print("Score:", round(item["score"], 3))
    print("Text:")
    print(item["document"].strip())
    print()
