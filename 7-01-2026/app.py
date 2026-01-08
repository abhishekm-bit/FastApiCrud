from services.embedding import generate_embedding
from services.vector_store import get_collection

# STEP 1: store data first
collection = get_collection()

text = "Can I know policy of Cascade Clouds?"
embedding = generate_embedding(text)

collection.add(
    ids=["query1"],
    embeddings=[embedding],
    documents=[text]
)

# STEP 2: search
query = "Can I know policy  Cascade ?"
query_embedding = generate_embedding(query)

result = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print(result)
