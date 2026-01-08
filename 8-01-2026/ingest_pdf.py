from services.pdf_loader import load_pdf_text
from services.chunker import chunk_text
from services.search import store_chunks
from services.vector_store import get_collection
import json
pdf_path = "data/Sample.pdf"

text = load_pdf_text(pdf_path)
chunks = chunk_text(text)

store_chunks(chunks)
# chunks means the whole pdf data is there
# print("chunks",json.dumps(chunks,indent=1))
# 


print("✅ PDF ingested and stored in vector DB")
print("PDF TEXT LENGTH:", len(text))
print(text[:500])

collection = get_collection()
print("AFTER INGEST → TOTAL CHUNKS IN DB:", collection.count())

print("\n--- GENERATED CHUNKS ---\n")
for i, chunk in enumerate(chunks, start=1):
    print(f"--- Chunk {i} ---")
    print(chunk)
    print("-" * 50)
