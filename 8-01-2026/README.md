#📄 PDF Similarity Search using RAG (Ollama + ChromaDB)
---
---
This project demonstrates a basic Retrieval-Augmented Generation (RAG) pipeline built from scratch using Python, Ollama embeddings, ChromaDB (Vector Database), and Cosine Similarity.
---
---
##The system:
Loads a PDF

Converts PDF text into chunks

Generates embeddings for each chunk

Stores embeddings in a vector database (ChromaDB)

Accepts user queries

Finds the most semantically similar chunks using cosine similarity

🛠 Tech Stack

Python 3.11

Virtual Environment (venv)

Ollama (nomic-embed-text model)

ChromaDB (vector database)

PyPDF

NumPy

Cosine Similarity

📁 Project Folder Structure
```
8-01-2026/
│
├── data/
│   └── sample.pdf                 # Input PDF file
│
├── chroma_db/                     # Persistent ChromaDB storage
│
├── services/
│   ├── pdf_loader.py              # Load PDF text
│   ├── text_splitter.py           # Chunking logic
│   ├── embedding.py               # Generate embeddings (Ollama)
│   ├── vector_store.py            # ChromaDB connection
│   ├── search.py                  # Store & query chunks
│   └── cosine_similarity.py       # Manual cosine similarity
│
├── ingest_pdf.py                  # PDF → chunks → embeddings → DB
├── query.py                       # Query → similarity search
├── requirements.txt               # Dependencies
├── .gitignore                     # Ignored files
├── README.md                      # Documentation
└── venv/                          # Virtual environment

```
⚙️ Setup Instructions (VERY IMPORTANT)
1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

2️⃣ Activate Virtual Environment
Windows

```bash
venv\Scripts\activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
Example requirements.txt:
```
chromadb
ollama
pypdf
numpy
```
4️⃣ Install Ollama & Embedding Model
Install Ollama from:

```bash
https://ollama.com
```

Then pull embedding model:
```bash
ollama pull nomic-embed-text
```

📥 Step 1: Ingest PDF into Vector Database
Run:
```bash
python ingest_pdf.py
```
What happens internally:

PDF text is loaded

Text is split into chunks (500 chars with 50 overlap)

Each chunk is converted into an embedding

Embeddings are stored in ChromaDB

Example output:

```
PDF TEXT LENGTH: 1379
AFTER INGEST → TOTAL CHUNKS IN DB: 4
✅ PDF ingested and stored in vector DB

```

🔍 Step 2: Query the PDF

Run:

```bash
python query.py
```

Example query:
```bash
query = "Who is Vishwas Narayan Nangare Patil?"
```

Example output:
```
--- Result 1 ---
Score: 0.615
Vishwas Narayan Nangare Patil, IPS, PPMG is an Indian Police Service officer...

--- Result 2 ---
Score: 0.525
Positions held...
```

✔ Higher score = more similar text

🧩 How Chunking Works

```bash
def chunk_text(text, chunk_size=500, overlap=50):
```
Each chunk contains 500 characters

50 characters overlap ensures context is preserved

Total chunks depend on PDF text length

Example:

PDF length = 1379

Chunk size = 500

Result = 4 chunks


```
🧠 What ChromaDB Stores

Each entry in ChromaDB contains:

id → chunk_0, chunk_1, etc.

embedding → list of ~768 numbers

document → original text chunk
```

```
🧪 Why Virtual Environment is Required

Prevents version conflicts (NumPy, ChromaDB)

Keeps project isolated

Industry best practice

Avoids Python 3.14 instability issues
```

```
🚀 What This Project Demonstrates

✔ RAG fundamentals
✔ Vector databases
✔ Embeddings
✔ Semantic search
✔ Cosine similarity
✔ Real-world GenAI workflow
```
