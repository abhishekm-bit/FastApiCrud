import chromadb 
import ollama

# created connection with database chromadb
client=chromadb.Client()


# table  named collection in the chromadb
collection=client.get_or_create_collection(name="queries")


# this is the text that want to convert into embedding
text="Can I Know Policy of the Cascade Clouds"

# embedding 
response=ollama.embeddings(
    model="nomic-embed-text",
    prompt=text
)
embedding=response["embedding"]

# added text to  db chromadb 
collection.add(
    ids=["quey1"], 
    # Unique ID for this entry

    embeddings=[embedding],
    # vector numbers 

    documents=[text]
    # actual text stored 
)
print("Completed Query embedded and Store into ChromaDb")