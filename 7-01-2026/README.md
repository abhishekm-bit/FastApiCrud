# Vector Embedding & Storage using Ollama and ChromaDB

This project demonstrates how to convert text into vector embeddings using
Ollama and store them in a ChromaDB vector database. It represents the
foundation of a RAG (Retrieval Augmented Generation) pipeline.

---

## Tech Stack
- Python 3.11
- Ollama (Embedding Model)
- ChromaDB (Vector Database)

---

## Project Structure
```
7-01-2026/
├── embed_store.py
├── app.py
├── services/
│ ├── embedding.py
│ ├── vector_store.py
│ └── search.py
├── api/
│ └── endpoints.py
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore

```


---

## Setup & Run

### 1. Create Virtual Environment
```bash
py -3.11 -m venv venv
venv\Scripts\activate

```

```bash
pip install -r requirements.txt
```

```bash
ollama pull nomic-embed-text
ollama list
```

```bash
python embed_store.py
```

## Output Completed Query embedded and Store into ChromaDb

```bash
python app.py
``` 
 ## This embeds a query and retrieves the most similar stored text.

# Screenshots Included

# Ollama model availability

# Embedding & storage execution

# Similarity search output

# Code implementation

## Summary

This project converts text into embeddings and stores them in a vector
database, enabling semantic search. This is the core building block
used in modern AI systems such as chatbots and RAG-based applications

